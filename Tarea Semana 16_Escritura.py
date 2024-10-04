#Primero creamos el archivo y definimos su nombre
file_name="my_notes.txt"
#Colocamos el modo escritura "w" (write // escribir)
arch_escritura=open(file_name,"w")
#Comando write: Permite escribir una linea por vez. Se coloca \n para realizar salto de linea
arch_escritura.write("Mi nombre es Charlie Cuaces. Vivo en la ciudad de Quito en la Parroquia de Cumbaya \n")
arch_escritura.write("Tengo 25 años de edad, naci el 01 de septiembre de 1999 \n")
#Comando writeline: Permite escribir lista de lineas
lineas = ["Recientemente termine mi primera carrera donde me titule como Tecnologo Superior en Redes y Telecomunicaciones \n",
          "Sigo la carrera de Tecnologias de la informacion porque desde pequeño me gusto."]
arch_escritura.writelines(lineas)
#Cerramos el archivo
arch_escritura.close()