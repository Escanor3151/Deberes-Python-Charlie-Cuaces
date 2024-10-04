file_name="my_notes.txt"
#Colocamos el modo lectura "r" (read // leer)
arch_lectura=open(file_name,"r")
#Comando read: lee todo el contenido del archivo
contenido_completo = arch_lectura.read()
print(contenido_completo)
print("")
#Comando readline: Lee una linea por vez
arch_lectura.seek(0) #Se reinicia el cursor al principio del archivo
#Seleccionamos la linea a leer
linea_1=arch_lectura.readline()
linea_2=arch_lectura.readline()
linea_3=arch_lectura.readline()
linea_4=arch_lectura.readline()
#Strip elimina el salto de linea
print("Linea 1: ", linea_1.strip())
print("Linea 2: ", linea_2.strip())
print("Linea 3: ", linea_3.strip())
print("Linea 4: ", linea_4.strip())
#Cerramos el archivo
arch_lectura.close()