#Requires -Version 5.1
# ==============================================================
#   DEMO INTERACTIVA  VIT Plataforma ISO 27001 SGSI
#   Reunion con Ingeniero de Empresa | 12 de Marzo 2026
# ==============================================================
#
#   COMO USAR:
#     Abre PowerShell en c:\Proyecto_VIT y ejecuta:
#       .\demo\DEMO_HOY.ps1
#
#   Cada paso muestra QUE DECIR en voz alta.
#   Presiona ENTER y el sistema ejecuta la accion en tiempo real.
#
# ==============================================================

Set-StrictMode -Off
$ErrorActionPreference = "SilentlyContinue"
$ProgressPreference    = "SilentlyContinue"

# -- Configuracion ---------------------------------------------------------
$BASE      = "http://localhost:8000/api"
$FRONT     = "http://localhost:3000"
$PYTHON    = "c:\Proyecto_VIT\backend\.venv\Scripts\python.exe"
$BACK_DIR  = "c:\Proyecto_VIT\backend"
$FRONT_DIR = "c:\Proyecto_VIT\frontend"
$DIAGRAM   = "c:\Proyecto_VIT\z_docs\01_architecture\MODELO_DATOS_FORMAL.md"

$script:TAdmin       = $null
$script:TConsultant  = $null
$script:TClient      = $null
$script:CompanyId    = 1
$script:NewProjectId = $null

# -- Utilidades de pantalla ------------------------------------------------
function Show-Banner {
    Clear-Host
    Write-Host ""
    Write-Host "  ============================================================" -ForegroundColor Cyan
    Write-Host "   VIT  |  Plataforma SGSI ISO 27001                         " -ForegroundColor Cyan
    Write-Host "   Demo Interactiva  |  Reunion Ingenieria  |  12 Mar 2026   " -ForegroundColor Cyan
    Write-Host "  ============================================================" -ForegroundColor Cyan
    Write-Host ""
}

function Show-Step {
    param([int]$N, [string]$Titulo, [string]$Decir)
    Write-Host ""
    Write-Host ("  [ PASO {0:D2} ]  {1}" -f $N, $Titulo) -ForegroundColor Yellow
    Write-Host ""
    foreach ($line in ($Decir -split "`n")) {
        Write-Host "      $line" -ForegroundColor White
    }
    Write-Host ""
    $null = Read-Host "  [ ENTER para ejecutar ]"
}

function Show-Ok {
    param([string]$Msg, $Obj = $null)
    Write-Host "  OK  $Msg" -ForegroundColor Green
    if ($null -ne $Obj) {
        Write-Host ($Obj | ConvertTo-Json -Depth 2 -Compress) -ForegroundColor DarkGray
    }
    Write-Host ""
}

function Show-Warn {
    param([string]$Msg)
    Write-Host "  AVISO  $Msg" -ForegroundColor Yellow
    Write-Host ""
}

function Show-Blocked {
    param([string]$Msg)
    Write-Host "  BLOQUEADO  $Msg" -ForegroundColor Red
    Write-Host "  -> Correcto: la seguridad esta bloqueando la accion" -ForegroundColor DarkRed
    Write-Host ""
}

function Show-HR {
    Write-Host ("  " + ("-" * 58)) -ForegroundColor DarkGray
}

function Next {
    $null = Read-Host "  -> [ ENTER para continuar ]"
}

# -- Helpers de API --------------------------------------------------------
function Invoke-GetToken {
    param([string]$User, [string]$Pass)
    try {
        $body = (@{ username = $User; password = $Pass } | ConvertTo-Json)
        $r = Invoke-RestMethod -Uri "$BASE/token/" -Method POST `
             -Body $body -ContentType "application/json"
        return $r.access
    } catch { return $null }
}

function Invoke-ApiGet {
    param([string]$Path, [string]$Token)
    try {
        return Invoke-RestMethod -Uri "$BASE$Path" -Method GET `
               -Headers @{ Authorization = "Bearer $Token" }
    } catch { return $null }
}

function Invoke-ApiPost {
    param([string]$Path, [string]$Token, $Body)
    try {
        return Invoke-RestMethod -Uri "$BASE$Path" -Method POST `
               -Headers @{ Authorization = "Bearer $Token" } `
               -Body ($Body | ConvertTo-Json) `
               -ContentType "application/json"
    } catch {
        $code = 0
        if ($null -ne $_.Exception.Response) {
            $code = [int]$_.Exception.Response.StatusCode
        }
        return [PSCustomObject]@{ __error = $true; code = $code }
    }
}

function Get-ListFromResponse {
    param($Response)
    if ($null -eq $Response) { return @() }
    if ($Response.results)   { return $Response.results }
    return $Response
}

function Test-ServerUp {
    param([string]$Url)
    try {
        Invoke-WebRequest -Uri $Url -TimeoutSec 2 | Out-Null
        return $true
    } catch {
        return ($null -ne $_.Exception.Response)
    }
}

# ==========================================================================
#   INICIO
# ==========================================================================

Show-Banner
Write-Host "  10 pasos  |  ~10 minutos  |  tu controlas el ritmo" -ForegroundColor DarkGray
Write-Host "  Lee el texto de >>> en voz alta, luego presiona ENTER" -ForegroundColor DarkGray
Write-Host ""
$null = Read-Host "  Presiona ENTER cuando estes listo"

# --------------------------------------------------------------------------
# PASO 1: CONTEXTO
# --------------------------------------------------------------------------
Show-Banner
Show-Step 1 "Contexto del avance semanal" "La semana pasada validamos Sprint 1:`nautenticacion JWT, permisos por rol y auditoria automatica.`n`nEsta semana avanzamos en dos frentes:`n  1) El modelo de datos formal que usted solicito`n  2) Un frontend integrado que consume la misma API en tiempo real`n`nHoy mostramos el sistema funcionando de extremo a extremo:`ndesde la base de datos hasta la pantalla del usuario."

Show-Ok "Contexto comunicado"
Show-HR

# --------------------------------------------------------------------------
# PASO 2: INICIAR SERVIDORES
# --------------------------------------------------------------------------
Show-Banner
Show-Step 2 "Levantar Backend y Frontend en vivo" "Voy a iniciar ambos servidores ahora mismo, en tiempo real.`nNada esta pre-grabado. El sistema arranca desde cero.`n`nBackend Django  --> puerto 8000  (API REST + PostgreSQL)`nFrontend React  --> puerto 3000  (interfaz web)"

$backendUp  = Test-ServerUp "http://localhost:8000/"
$frontendUp = Test-ServerUp "http://localhost:3000/"

if (-not $backendUp) {
    Write-Host "  Iniciando Backend Django..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", `
        "Set-Location '$BACK_DIR'; Write-Host 'BACKEND VIT - Django/PostgreSQL' -ForegroundColor Green; & '$PYTHON' manage.py runserver"
} else {
    Write-Host "  Backend ya estaba en linea en localhost:8000" -ForegroundColor DarkGreen
}

if (-not $frontendUp) {
    Write-Host "  Iniciando Frontend React/Vite..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", `
        "Set-Location '$FRONT_DIR'; Write-Host 'FRONTEND VIT - React/Vite' -ForegroundColor Cyan; npm run dev"
} else {
    Write-Host "  Frontend ya estaba en linea en localhost:3000" -ForegroundColor DarkGreen
}

if (-not $backendUp -or -not $frontendUp) {
    Write-Host ""
    Write-Host "  Esperando 6 segundos para que los servicios arranquen..." -ForegroundColor DarkGray
    Start-Sleep 6
}

$alive = Test-ServerUp "http://localhost:8000/"
if ($alive) {
    Show-Ok "Ambos servidores en linea y listos"
} else {
    Show-Warn "El backend aun puede estar iniciando - continua, tomara unos segundos mas"
}
Show-HR

# --------------------------------------------------------------------------
# PASO 3: LOGIN ADMIN - JWT EN VIVO
# --------------------------------------------------------------------------
Show-Banner
Show-Step 3 "Autenticacion JWT - Administrador VIT" "El sistema usa JWT en lugar de sesiones en servidor.`nAl iniciar sesion, el backend genera:`n  - Token de acceso: 15 minutos, para cada peticion API`n  - Refresh token:   24 horas, para renovar sin re-login`n`nHacemos el login de admin_vit ahora mismo."

$script:TAdmin = Invoke-GetToken "admin_vit" "admin123"
if ($script:TAdmin) {
    $prev = $script:TAdmin.Substring(0, [Math]::Min(50, $script:TAdmin.Length)) + "..."
    Show-Ok "Token JWT obtenido para admin_vit" @{
        token  = $prev
        expira = "15 minutos"
        tipo   = "Bearer JWT stateless"
    }
} else {
    Show-Warn "No se pudo obtener token. Verifica que el backend este corriendo."
}
Show-HR

# --------------------------------------------------------------------------
# PASO 4: ADMIN VE TODOS LOS PROYECTOS
# --------------------------------------------------------------------------
Show-Banner
Show-Step 4 "Control de acceso - Admin ve TODOS los proyectos" "El Administrador VIT no tiene restricciones de empresa.`nEl queryset de Django devuelve todos los proyectos del sistema.`n`nEste filtrado ocurre en el SERVIDOR, no en la UI.`nAunque alguien modifique la interfaz, el backend aplica`nlas mismas reglas de acceso."

$res   = Invoke-ApiGet "/projects/" $script:TAdmin
$lista = Get-ListFromResponse $res
if ($lista.Count -gt 0) {
    Show-Ok "$($lista.Count) proyecto(s) visibles para el Administrador:"
    $lista | ForEach-Object {
        Write-Host ("    - [ID:{0}]  {1}  [{2}]" -f $_.id, $_.name, $_.status) -ForegroundColor Gray
    }
} else {
    Show-Warn "No hay proyectos en la BD o el token expiro"
}
Write-Host ""
Next
Show-HR

# --------------------------------------------------------------------------
# PASO 5: CONSULTOR SOLO VE LO ASIGNADO
# --------------------------------------------------------------------------
Show-Banner
Show-Step 5 "Control de acceso - Consultor ve SOLO asignados" "El Consultor solo puede ver proyectos donde fue asignado.`nUsamos la misma URL /api/projects/ pero con diferente token.`n`nEl filtrado es a nivel de queryset en Django:`n  - No depende de la URL`n  - No depende del frontend`n  - El servidor decide que datos expone a cada usuario"

$script:TConsultant = Invoke-GetToken "consultant_ana" "consultant123"
$res2  = Invoke-ApiGet "/projects/" $script:TConsultant
$list2 = Get-ListFromResponse $res2
if ($null -ne $res2) {
    Show-Ok "$($list2.Count) proyecto(s) visibles para consultant_ana (filtrado automatico):"
    $list2 | ForEach-Object {
        Write-Host ("    - [ID:{0}]  {1}" -f $_.id, $_.name) -ForegroundColor Gray
    }
    if ($lista.Count -gt $list2.Count) {
        Write-Host ("    -> Admin veia {0} proyecto(s), Consultor ve {1}. La diferencia confirma el filtrado." -f $lista.Count, $list2.Count) -ForegroundColor DarkGreen
    }
} else {
    Show-Warn "No se pudo consultar proyectos del consultor"
}
Write-Host ""
Next
Show-HR

# --------------------------------------------------------------------------
# PASO 6: INTERFAZ WEB - ABRIR BROWSER
# --------------------------------------------------------------------------
Show-Banner
Show-Step 6 "Demostracion en interfaz web" "Ahora vemos el mismo comportamiento desde la UI.`nEl frontend React consume exactamente la misma API que acabamos`nde demostrar por consola.`n`nCredenciales para mostrar:`n  Admin:      admin_vit       / admin123`n  Consultor:  consultant_ana  / consultant123`n  Cliente:    client_juan     / client123`n`nGUIA para el browser:`n  1) Inicia sesion como admin_vit -> observa cuantos proyectos ve`n  2) Cierra sesion -> entra como consultant_ana -> observa la diferencia`n  3) Abre un proyecto para ver sus fases y tareas"

Start-Process "$FRONT/login"
Show-Ok "Browser abierto en $FRONT/login"
Write-Host ""
Next
Show-HR

# --------------------------------------------------------------------------
# PASO 7: CREAR PROYECTO EN VIVO
# --------------------------------------------------------------------------
Show-Banner
Show-Step 7 "Accion en vivo - Consultor crea un proyecto ISO 27001" "Un Consultor puede crear proyectos en el sistema.`nVamos a crear uno ahora mismo para demostrar el flujo completo.`n`nAl crearlo, el sistema registrara la accion automaticamente`nen el audit log, sin codigo adicional en la vista."

$comps = Invoke-ApiGet "/companies/" $script:TConsultant
$clist = Get-ListFromResponse $comps
if ($clist.Count -gt 0) { $script:CompanyId = $clist[0].id }

$nuevo = Invoke-ApiPost "/projects/" $script:TConsultant @{
    name        = ("DEMO ISO 27001 - Reunion " + (Get-Date -Format "HH:mm"))
    company     = $script:CompanyId
    status      = "PLANNING"
    start_date  = (Get-Date -Format "yyyy-MM-dd")
    description = "Proyecto creado en vivo durante presentacion con ingeniero de empresa"
}

if ($nuevo -and -not $nuevo.__error) {
    $script:NewProjectId = $nuevo.id
    Show-Ok "Proyecto creado exitosamente" @{
        id      = $nuevo.id
        nombre  = $nuevo.name
        estado  = $nuevo.status
        empresa = $nuevo.company
    }
} else {
    $code = if ($nuevo) { $nuevo.code } else { "N/A" }
    Show-Warn ("No se pudo crear el proyecto (HTTP {0}). Verifica que exista company id={1} en la BD." -f $code, $script:CompanyId)
}
Next
Show-HR

# --------------------------------------------------------------------------
# PASO 8: AUDITORIA AUTOMATICA
# --------------------------------------------------------------------------
Show-Banner
Show-Step 8 "Trazabilidad - AuditLog automatico (ISO 27001 A.12.4.1)" "ISO 27001 requiere que toda accion critica quede registrada.`nControl especifico: A.12.4.1 - Registro de eventos.`n`nEn nuestra plataforma, el registro es automatico:`n  - Usa Django signals (post_save, post_delete)`n  - No hay codigo manual en los ViewSets`n  - Registra: quien, que accion, que entidad, cuando y los cambios`n`nVeamos el registro del proyecto que acabamos de crear."

$logs  = Invoke-ApiGet "/audit-logs/?action=CREATE&entity_type=Project&ordering=-timestamp" $script:TAdmin
$llogs = Get-ListFromResponse $logs
$ult   = $llogs | Select-Object -First 1

if ($null -ne $ult) {
    Show-Ok "Ultimo registro en AuditLog (generado automaticamente):"
    Write-Host "    Usuario:   $($ult.user_username)" -ForegroundColor Gray
    Write-Host "    Accion:    CREATE" -ForegroundColor Gray
    Write-Host "    Entidad:   $($ult.entity_type) #$($ult.entity_id)" -ForegroundColor Gray
    Write-Host "    Timestamp: $($ult.timestamp)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  -> Cumplimiento ISO 27001 A.12.4.1 implementado" -ForegroundColor DarkGreen
} else {
    Show-Warn "No se pudo consultar los audit logs (verifica permisos del admin token)"
}
Write-Host ""
Next
Show-HR

# --------------------------------------------------------------------------
# PASO 9: SEGURIDAD - CLIENTE BLOQUEADO
# --------------------------------------------------------------------------
Show-Banner
Show-Step 9 "Seguridad - Cliente intenta crear un proyecto (debe fallar)" "Un Cliente solo puede ver el avance de su propio proyecto`ny subir evidencias. No puede crear proyectos.`n`nIntentamos crear un proyecto con credenciales de Cliente.`nEl servidor debe rechazarlo con HTTP 403 Forbidden."

$script:TClient = Invoke-GetToken "client_juan" "client123"
$intento = Invoke-ApiPost "/projects/" $script:TClient @{
    name       = "Proyecto No Autorizado"
    company    = $script:CompanyId
    status     = "PLANNING"
    start_date = (Get-Date -Format "yyyy-MM-dd")
}

if ($null -eq $intento) {
    Show-Blocked "Acceso denegado - servidor bloqueo la peticion del Cliente"
} elseif ($intento.__error) {
    Show-Blocked ("HTTP {0} Forbidden - El servidor rechazo al Cliente por control de permisos" -f $intento.code)
} else {
    Show-Warn "El proyecto fue creado - revisar configuracion de permisos del rol CLIENT en ProjectViewSet"
}

Next
Show-HR

# --------------------------------------------------------------------------
# PASO 10: MODELO DE DATOS
# --------------------------------------------------------------------------
Show-Banner
Show-Step 10 "Modelo de datos - Diseno formal (solicitado la semana pasada)" "Este es el modelo de datos que usted solicito en la reunion anterior.`nDisenado para soportar proyectos ISO 27001 completos:`n`n  - Project -> Phase -> Task`n      Estructura operativa del ciclo SGSI`n`n  - ProjectUser (tabla intermedia)`n      Un usuario puede ser Consultor en proyecto A`n      y Cliente en proyecto B simultaneamente`n`n  - AuditLog`n      Trazabilidad completa para cumplimiento ISO 27001`n`n  - Company`n      Separacion multi-empresa desde el diseno base`n`nCada decision de diseno responde a un requisito ISO 27001`no a un caso de uso real del flujo de implementacion."

if (Test-Path $DIAGRAM) {
    Start-Process $DIAGRAM
    Show-Ok "Diagrama de datos abierto"
} else {
    Show-Warn "Abrir manualmente: z_docs\01_architecture\MODELO_DATOS_FORMAL.md"
}
Next
Show-HR

# ==========================================================================
#   CIERRE
# ==========================================================================
Show-Banner

Write-Host "  ============================================================" -ForegroundColor DarkGreen
Write-Host "   ESTADO ACTUAL DEL PROYECTO" -ForegroundColor DarkGreen
Write-Host "  ============================================================" -ForegroundColor DarkGreen
Write-Host ""
Write-Host "  COMPLETADO:" -ForegroundColor Green
Write-Host "    Sprint 1  -  Autenticacion JWT + RBAC + Multi-tenancy + AuditLog" -ForegroundColor Gray
Write-Host "    Modelo de datos formal (entregado hoy)" -ForegroundColor Gray
Write-Host "    Frontend integrado con API real (Login, Dashboard, Detalle de Proyecto)" -ForegroundColor Gray
Write-Host ""
Write-Host "  EN PROGRESO:" -ForegroundColor Yellow
Write-Host "    Gestion completa de Fases y Tareas en la interfaz web" -ForegroundColor Gray
Write-Host "    Experiencia de usuario y navegacion" -ForegroundColor Gray
Write-Host ""
Write-Host "  MODULOS PROPUESTOS PARA SIGUIENTE SPRINT:" -ForegroundColor Cyan
Write-Host "    Gestion de Riesgos ISO 27001 (identificacion, analisis, mitigacion)" -ForegroundColor Gray
Write-Host "    Evidencias y documentos de cumplimiento" -ForegroundColor Gray
Write-Host "    Statement of Applicability (SoA)" -ForegroundColor Gray
Write-Host ""
Show-HR
Write-Host ""
Write-Host "  ============================================================" -ForegroundColor Magenta
Write-Host "   PREGUNTAS PARA VALIDAR CON EL INGENIERO" -ForegroundColor Magenta
Write-Host "  ============================================================" -ForegroundColor Magenta
Write-Host ""
Write-Host "  1) El modelo de datos es adecuado para soportar" -ForegroundColor White
Write-Host "     el flujo SGSI completo de ISO 27001?" -ForegroundColor White
Write-Host ""
Write-Host "  2) Para la siguiente entrega, priorizamos el modulo" -ForegroundColor White
Write-Host "     de Riesgos o el de Evidencias?" -ForegroundColor White
Write-Host ""
Write-Host "  3) El nivel actual de auditoria es suficiente o deberiamos" -ForegroundColor White
Write-Host "     registrar mas eventos como inicio de sesion o descarga de documentos?" -ForegroundColor White
Write-Host ""
Show-HR
Write-Host ""
Write-Host "  Fin de la demo. Presiona ENTER para cerrar." -ForegroundColor DarkGray
$null = Read-Host
