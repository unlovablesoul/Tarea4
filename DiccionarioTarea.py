#Creación de Directorio para la tarea 4 del curso de Programación


NotasA ={"Programacion":["7.0","6,5","6.9"],"Fisica":["7.0","5,7","5.9"]}
NotasB ={"Programacion":["6.0","4,5","3.9"],"Fisica":["4.0","4,5","4.9"]}
NotasC ={"Programacion":["5.0","2,5","5.9"],"Fisica":["6.0","5,1","3.9"]}
NotasD ={"Programacion":["3.0","5,5","4.9"],"Fisica":["5.0","5,3","5.9"]}
Alumnos = {"Eric Cardenas":NotasA,"Claudio Filunir":NotasB,"Lucas Urrutia":NotasC,"Cristobal Dodoria":NotasD}
cont=1
print("Seleccione la opcion del alumno que desea ver las notas")
opciones={}
for key in Alumnos:
    opc =key
    print(str(cont) + ".- " + key)
    opciones[str(cont)]=key
    cont = cont + 1
mostrar = input("\n")
print(mostrar)