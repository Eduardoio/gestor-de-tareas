import datetime  # aqui lo que hace datetime es darle una libreria a python para que lea dia,mesaños y horas #

nombre_de_tarea = input("el nombre de la tarea es: ")
fecha_de_entrega = input("dia,mes,año: ")
# TOMA EL TEXTO QUE INGRESA EL USUARIO USA EL MOLDE PARA SABER DONDE ESTA EL DIA Y ESO Y LUEGO LO TRANSFORMA A FECHA REAL Y YA PHYTON SI PUEDE HACER OPERACIONES
fecha_convertida = datetime.datetime.strptime(fecha_de_entrega, "%d/%m/%Y")
alerta = datetime.timedelta(days=2)
fecha_de_alerta = fecha_convertida-alerta
print(fecha_de_alerta)
archivo = open("gestor_de_tareas.txt", "a")
archivo.write(nombre_de_tarea + "-se entrega el:  " +
              fecha_de_entrega + "-alerta: " + str(fecha_de_alerta)+"\n")
archivo.close()
print("tarea guardada exitosamente")
