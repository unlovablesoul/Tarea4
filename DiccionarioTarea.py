#Creación de Directorio para la tarea 4 del curso de Programación


NotasA ={"Programacion":["5.3","6,5","6.9"],"Fisica":["5.4","5,7","5.9"]}
NotasB ={"Programacion":["6.0","4,5","3.9"],"Fisica":["4.0","4,5","4.9"]}
NotasC ={"Programacion":["5.0","2,5","5.9"],"Fisica":["6.0","5,1","3.9"]}
NotasD ={"Programacion":["3.0","5,5","4.9"],"Fisica":["5.0","5,3","5.9"]}
Alumnos = {"Eric Cardenas":NotasA,"Claudio Filunir":NotasB,"Lucas Urrutia":NotasC,"Cristobal Dodoria":NotasD}

while True:
    cont=1
    print("Seleccione la opcion del alumno que desea ver las notas")
    opciones={}
    for key in Alumnos:
        opc =key
        print(str(cont) + ".- " + key)
        opciones[str(cont)]=key
        cont = cont + 1
    print("5.- Salir")
    mostrar = input("\n")
    if mostrar == "5":
        print("Adios")
        break
    elif int(mostrar)>cont+1:
        print("Seleccione una opcion correcta")
        continue
    nota = Alumnos[opciones[mostrar]]
    print("\nQue notas desea ver(Ingrese opcion): \n")
    print("1.- Programacion")
    print("2.- Fisica")
    notaelegida = input("\n")
    llave = "a"
    if notaelegida == "1":
        print("\nMostrando notas de programacion")
        llave = "Programacion"
    elif notaelegida == "2":
        print("\nMostrando notas de Fisica\n")
        llave = "Fisica"
    else:
        print("Seleccione una opcion correcta porfavor")

    if llave != "a":
        cont=1
        for calificacion in nota[llave]:
            print("Nota " + str(cont) + ": " + calificacion)
            cont = cont + 1
        print("\n")