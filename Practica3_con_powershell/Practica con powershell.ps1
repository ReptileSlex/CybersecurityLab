Write-Host
Write-Host "Este programa obtiene datos de la computadora en uso y los exporta a un archivo txt donde ha sido ejecutado"
Write-Host "Los datos exportados los encontrarás donde ejecutaste este programa"
Write-Host 
Write-Host "1 - Obtener archivos de un tipo accesados a partir de una fecha dada"
Write-Host "2 - Obtener los datos de tu PC"
Write-Host " "
[int32] $opcion = Read-Host -Prompt "Selecciona una de las opciones mencionadas arriba"

Function archivos_accesados {
    param(
    [string] $ruta ,
    [string] $extension ,
    [string] $extension1 ,
    [datetime] $fecha
    )

# Si en los parametros no se especifica la fecha se muestran los archivos accesados el último año
    if (!$fecha){
        $fecha=(Get-Date).AddDays(-365)
    }
Get-ChildItem -Path $ruta -Include *.$extension -Recurse -File | Where-Object {$_.LastAccessTime -ge $fecha}
# Get-ChildItem -Path $ruta -Include *.$extension1 -Recurse -File | Where-Object {$_.LastAccessTime -ge $fecha} # Esta linea es opcional
}

Function datos_pc{
    Write-Host
    Write-Host "Información de CPU" 
    Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty "CIM*" 
    Get-CimInstance -ClassName Win32_ComputerSystem
    Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3"
    Write-Host "Tarjeta Gráfica" | Get-WmiObject win32_VideoController | Format-List Name
    Write-Host "Tiempo de uso"
    (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime
}

if ($opcion -eq 1 ){
    archivos_accesados -ruta "D:\Downloads" -extension "pdf" -extension1 "txt" | Out-File -FilePath .\archivosaccesados.txt
}
elseif($opcion -eq 2){
    datos_pc | Out-File -FilePath .\datospc.txt
}
else{
Write-Host "Esa opcion no existe"
}