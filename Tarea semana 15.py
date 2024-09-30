#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona,
#incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
informacion_personal= {"Nombre":"Charlie Cuaces", "Edad":"25", "Ciudad":"Qu1ito"}
print (informacion_personal)
fin = False #Ocuparemos la variable fin que se mantenga en falso hasta que se desee culminar el programa
while not fin:  # Se trabajara con un While para poder repetir el menu si el cliente lo desea
    print("""
              Menu Principal: Elija Opcion
              1. Agregar o Validar 
              2. Modificar
              3. Eliminar
              4. Imprimir tabla final  
              5. Salir
            """) #Se imprime menu
    op = int(input("Opcion: "))#Se le la opcion que desee
    match op:#Segun la opcion elegida se ingresara y realizara el requerimiento solicitado
        case 1:
            print("Primero validaremos si la clave que quiere ingresar ya existe, sino se agregara")
            clave_nueva=(input("Nombre de la clave: "))
            if clave_nueva in informacion_personal: #Se crea un in para validar si la nueva clave que queremos ingresar existe o no.
                print("Si existe la clave" ,clave_nueva)
            else:
                # Si no existe se agregara la clave con su respectivo valor
                print("No existe la clave, vamos a agregarla")
                valor=(input("Ingrese valor de la clave: "))
                informacion_personal[clave_nueva]= valor
        case 2:
            #Guardamos en una variable la clave que deseamos modificar
            clave_modificar=(input("¿Que clave desea modificar?"))
            #Guardamos en una variable el valor que vamos a modificar
            valor_modificar=(input("Ingrese nuevo valor de la clave: "))
            #Asignamos el valor modificado en el diccionario
            informacion_personal[clave_modificar]=valor_modificar
        case 3:
            #Guardamos en una variable la clave a eliminar
            valor_eliminar=(input("Ingrese la clave a eliminar: "))
            #Asignamos la variable el comando emilinar del diccionario
            del(informacion_personal[valor_eliminar])
        case 4:
            #Imprimimos el diccionario modificado
            print(informacion_personal)
        case 5:
            print("A sido un gusto ")  # Opcion de salir y termina programada
            fin = True  # Fin ahora es verdadero y finaliza el programa