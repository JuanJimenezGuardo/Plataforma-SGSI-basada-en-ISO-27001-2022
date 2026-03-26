# Entregable Día 3: Guía de Validaciones UX y Manejo de Errores (Frontend)

**Responsable:** Luis (Frontend)
**Fecha:** 26 de Marzo de 2026
**Objetivo:** Estandarizar cómo la interfaz de usuario (React) reacciona ante las validaciones de formularios, respuestas de la API y caídas del sistema, garantizando una buena experiencia de usuario (UX).

---

## 1. Manejo Global de Códigos HTTP (Axios Interceptors)

Toda petición realizada a través de `api/axios.js` pasará por un interceptor global que mostrará los siguientes mensajes al usuario dependiendo del código de error:

| Código HTTP | Categoría | Comportamiento UX en la Interfaz |
| :--- | :--- | :--- |
| **400** | *Bad Request / Validación* | **No mostrar alerta global invasiva.** Leer el JSON de error y pintar el texto en color rojo (`var(--danger)`) justo debajo del input específico que falló. |
| **401** | *Unauthorized* | **Redirección automática.** Limpiar `localStorage`, mostrar Toast: *"Sesión expirada. Por favor, ingresa nuevamente."* y redirigir a `/login`. |
| **403** | *Forbidden / Permisos* | **Banner o pantalla de bloqueo.** Mostrar modal/banner: *"Acceso denegado. No tienes los permisos suficientes (Rol actual) para realizar esta acción."* No sacar al usuario de la app. |
| **500+** | *Server Error / Fallback* | **Toast de error general.** *"Error interno del servidor. Nuestros ingenieros han sido notificados."* Mantener la UI estable sin "pantallas blancas de la muerte". |

---

## 2. Reglas de Validación en Formularios (Antes de enviar a la API)

Para evitar sobrecargar el backend, el frontend validará estos criterios usando React Hook Form o validación manual antes de ejecutar el `POST`/`PATCH`:

### A. Formulario de Contactos (`Contact`)
* **Nombre completo:** Requerido. Máximo 150 caracteres.
* **Correo electrónico:** Requerido. Formato válido de email (Regex).
* **Rol en el proyecto:** Requerido. Solo seleccionar del desplegable (basado en Enum del backend).

### B. Formulario de Fases y Tareas (`Fechas Planned/Actual`)
* **Fechas Planificadas:** `planned_start_date` y `planned_end_date` son obligatorias al crear una fase.
* **Lógica Cruzada de Fechas:** * La *Fecha de Fin* (Planeada o Real) **nunca** puede ser menor a la *Fecha de Inicio* (Planeada o Real).
    * El frontend bloqueará el botón de "Guardar" y mostrará error: *"La fecha de finalización no puede ser anterior al inicio."*
* **Fechas Reales Nulas:** `actual_start_date` y `actual_end_date` son opcionales. El usuario puede dejarlas en blanco y el frontend enviará explícitamente `null`.

### C. Módulo de Documentos (`Document`)
* **Tamaño máximo:** Bloquear subida en el frontend si el archivo supera los 10MB. Alerta UX: *"El archivo es demasiado pesado (Máx 10MB)."*
* **Formatos permitidos:** Limitar el input a `.pdf, .docx, .xlsx, .png, .jpg`.

---

## 3. Fallbacks Visuales (Estados Vacíos y Carga)

* **Loaders:** Mientras se espera el endpoint (ej. `loading === true`), mostrar un texto o spinner sutil: *"Sincronizando con el servidor..."* en lugar de una pantalla congelada.
* **Empty States (Listas Vacías):** Si un proyecto no tiene contactos o fases (`length === 0`), renderizar una tarjeta con opacidad baja: *"No se encontraron registros. Haz clic en '+' para agregar el primero."*