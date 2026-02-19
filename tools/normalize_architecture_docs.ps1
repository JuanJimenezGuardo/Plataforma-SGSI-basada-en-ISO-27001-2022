$root = "c:\Proyecto_VIT"
$files = Get-ChildItem -Path "$root\architecture" -Filter *.md

$replacements = @(
    @{ From = "ISO/IEC 700:0"; To = "ISO/IEC 27001:2022" },
    @{ From = "ISO 700:0"; To = "ISO 27001:2022" },
    @{ From = "ISO 700"; To = "ISO 27001" },
    @{ From = "ISO 27001:2022para"; To = "ISO 27001:2022 para" },
    @{ From = "ISO 27001para"; To = "ISO 27001 para" },
    @{ From = "ISO 27001A.8."; To = "ISO 27001 A.8" },
    @{ From = "ISO 27001A.8"; To = "ISO 27001 A.8" },

    @{ From = "9controles"; To = "93 controles" },
    @{ From = "9items"; To = "93 items" },
    @{ From = "9SoAItems"; To = "93 SoAItems" },
    @{ From = "9registros"; To = "93 registros" },

    @{ From = "QUErySets"; To = "QuerySets" },
    @{ From = "QUEryset"; To = "queryset" },
    @{ From = "get_QUEryset"; To = "get_queryset" },
    @{ From = "QUEry"; To = "Query" },
    @{ From = "reQUEst"; To = "request" },
    @{ From = "ReQUEst"; To = "Request" },

    @{ From = "reQUEiere"; To = "requiere" },
    @{ From = "ReQUEiere"; To = "Requiere" },
    @{ From = "reQUErido"; To = "requerido" },
    @{ From = "ReQUErido"; To = "Requerido" },
    @{ From = "reQUErida"; To = "requerida" },
    @{ From = "ReQUErida"; To = "Requerida" },
    @{ From = "reQUEisito"; To = "requisito" },
    @{ From = "reQUEisitos"; To = "requisitos" },
    @{ From = "ReQUEisito"; To = "Requisito" },
    @{ From = "reQUEirements"; To = "requirements" },
    @{ From = "ReQUEirements"; To = "Requirements" },

    @{ From = "seQUEnce"; To = "sequence" },
    @{ From = "conseQUEnces"; To = "consecuencias" },
    @{ From = "conseQUEnce"; To = "consecuencia" },
    @{ From = "eQUEipo"; To = "equipo" },
    @{ From = "ArQUEitectonico"; To = "Arquitectonico" },
    @{ From = "AntioQUEia"; To = "Antioquia" },
    @{ From = "BloQUEante"; To = "Bloqueante" },
    @{ From = "bloQUEada"; To = "bloqueada" },
    @{ From = "riQUEza"; To = "riqueza" },
    @{ From = "snica"; To = "unica" },
    @{ From = "sltima"; To = "Ultima" },

    @{ From = "QUEI?N"; To = "QUIEN" },
    @{ From = "QUE?"; To = "QUE" },
    @{ From = "CUaNDO"; To = "CUANDO" },
    @{ From = "QUEe"; To = "que" },
    @{ From = "QUEda"; To = "queda" },
    @{ From = "queien"; To = "quien" },
    @{ From = "Queien"; To = "Quien" },
    @{ From = "quearterly"; To = "quarterly" },
    @{ From = "arqueitectonico"; To = "arquitectonico" },
    @{ From = "Equeipo"; To = "Equipo" },
    @{ From = "UNIque"; To = "UNIQUE" },
    @{ From = "UNIqueness"; To = "Uniqueness" },
    @{ From = "UNIque_together"; To = "unique_together" },
    @{ From = "UNIque INDEX"; To = "UNIQUE INDEX" },
    @{ From = "ISO 27001exige"; To = "ISO 27001 exige" }
)

foreach ($f in $files) {
    $text = Get-Content -Raw -LiteralPath $f.FullName -Encoding UTF8

    foreach ($r in $replacements) {
        $text = $text.Replace($r.From, $r.To)
    }

    # Normalize bullets that became dot-prefixed
    $text = [regex]::Replace($text, '(?m)^\.\s+', '- ')

    # Normalize arrows and relations
    $text = $text.Replace('<= ->', '<->')
    $text = $text.Replace('<= ->', '<->')

    # Collapse repeated spaces
    $text = [regex]::Replace($text, ' {2,}', ' ')

    [System.IO.File]::WriteAllText($f.FullName, $text, (New-Object System.Text.UTF8Encoding($false)))
}
