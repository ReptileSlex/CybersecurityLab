#!/bin/bash
echo "------------------------------Práctica laboratorio de programación en bash-----------------------------"
echo "El programa exporta los datos recolectados en archivos de texto en la ruta donde se ejecute el programa"
echo " 1 - Ver datos de tu pc"
echo " 2 - Exportar servicios ejecutandose después del script"
echo " 3 - Hacer copia de seguridad de una carpeta"
read opcion

verdatospc(){
uname -a
echo
lshw -short
echo
lscpu
echo
df -H
echo
free -ht
}

verservicios(){
ps -u
}

copiadeseguridad(){
FECHA=`date +%b-%d-%y` 
CARPETADESTINO=backup-$FECHA.tar.gz 
CARPETAORIGEN=/mnt/d/Users/buzza/Documents/UANL/Programación/ 
tar -cpzf $CARPETADESTINO $CARPETAORIGEN
}

if [ $opcion -eq 1 ];
then
verdatospc > datospc.txt
elif [ $opcion -eq 2 ];
then
verservicios > servicios.txt
elif [ $opcion -eq 3 ];
then
copiadeseguridad
fi
