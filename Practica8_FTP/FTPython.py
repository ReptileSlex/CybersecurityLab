# Alejandro de Jesús López Díaz Mat: 1990072
import os
import ftplib

txt = open("1990072.txt", "w")  # Creando y escribiendo en el archivo de texto
txt.write("Por qué me descargaste? D:  ...   Soy un virus c:")
txt.close()
print("Archivo de texto creado")

ftp = ftplib.FTP("ftp.dlptest.com")
ftp.login("dlpuser@dlptest.com", "eUj8GeW55SvYaswqUyDSm5v6N")

print("Descargando csv...")
ftp.retrbinary("RETR csv.csv", open('csv.csv', 'wb').write)
# ftp.retrbinary("RETR 1990072.txt", open('eskelersifuncionó', 'wb').write)

print("Subiendo 1990072.txt")
txt = open("1990072.txt", "rb")
ftp.storbinary("STOR 1990072.txt", txt)
ftp.retrlines("list")

ftp.quit()
