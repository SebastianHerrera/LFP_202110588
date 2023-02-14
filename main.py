from colorama import Fore
from tkinter import *
from tkinter import filedialog
import csv
from pelicula import Pelicula
import graphviz
import os
import webbrowser

root = Tk()
root.withdraw()
movies = []
actores = []
id = 0

print(Fore.YELLOW+"Curso: "+Fore.GREEN+"Lenguajes Formales y de Programación B+")
print(Fore.YELLOW+"Nombre: "+Fore.GREEN+"Geovanny Sebastián Herrera Claudio")
print(Fore.YELLOW+"Carné: "+Fore.GREEN+"202110588")

state = 0
while state==0:
    input()
    print(Fore.BLUE+"========MENÚ PRINCIPAL========")
    print(Fore.BLUE+"1. "+Fore.WHITE+"Cargar Archivo de Entrada")
    print(Fore.BLUE+"2. "+Fore.WHITE+"Gestionar Películas")
    print(Fore.BLUE+"3. "+Fore.WHITE+"Filtrado")
    print(Fore.BLUE+"4. "+Fore.WHITE+"Gráfica")
    print(Fore.BLUE+"5. "+Fore.WHITE+"Salir")
    print()
    print()
    option = int(input(Fore.BLUE+"Ingrese una opción: "+Fore.WHITE))
    if option == 1:
        i=0
        file = filedialog.askopenfilename(initialdir="C:/Users/sebas/Documents/USAC/Primer Semestre 2023/Lab LFP/Práctica 1/Archivos de Entrada",title="Elige un archivo de entrada", filetypes=(("Archivos de Datos","*.csv*"),("Todos los archivos","*.*")))
        with open(file,"r") as archivo:
            lector = csv.reader(archivo, delimiter=";")
            for fila in lector:
                nombre = str(fila[0])
                actores = str(fila[1])
                año = int(fila[2])
                genero = str(fila[3])
                if i == 0:
                    id = id+1
                    movies.append(Pelicula(id,nombre,actores,año,genero))
                    i=1
                else:
                    varval=1
                    for movie in movies:
                        if movie.nombre == nombre:
                            print()
                            print(Fore.RED+"La película "+nombre+" se ha intentado agregar más de una vez.")
                            varval = 0
                    if varval == 1:
                        id = id+1
                        movies.append(Pelicula(id,nombre,actores,año,genero))


    elif option == 2:
        print("     "+Fore.BLUE+"a. "+Fore.WHITE+"Mostrar Películas")
        print("     "+Fore.BLUE+"b. "+Fore.WHITE+"Gestionar Películas")
        opcion = input(Fore.BLUE+"Ingrese una opción: "+Fore.WHITE)
        if opcion == "a":
            print()
            for impresion in movies:
                print(Fore.WHITE+str(impresion.id),Fore.YELLOW+impresion.nombre,Fore.GREEN+impresion.actores,Fore.RED+str(impresion.año),Fore.BLACK+impresion.genero)
            print()
        elif opcion == "b":
            for impresion in movies:
                print(Fore.WHITE+str(impresion.id),Fore.YELLOW+impresion.nombre)
            print()
            movie = int(input(Fore.GREEN+"Ingrese el número de la película de la que desea saber sus actores:   "+Fore.WHITE))
            for index in movies:
                if index.id == movie:
                    print()
                    print(Fore.YELLOW+impresion.nombre)
                    print(Fore.WHITE+"ACTORES: "+Fore.BLUE+impresion.actores)
                    print()
        else:
            print(Fore.RED+"La opción ingresada no es correcta.")

    elif option == 3:
        print("     "+Fore.BLUE+"a. "+Fore.WHITE+"Filtrado por actor")
        print("     "+Fore.BLUE+"b. "+Fore.WHITE+"Filtrado por año")
        print("     "+Fore.BLUE+"c. "+Fore.WHITE+"Filtrado por género")
        opcion = input(Fore.BLUE+"Ingrese una opción: "+Fore.WHITE)
        if opcion == "a":
            print()
            actor = input(Fore.BLUE+"Nombre del actor: "+Fore.WHITE)
            print()
            print(Fore.GREEN+actor,Fore.WHITE+" actua en:")
            print()
            for impresion in movies:
                if impresion.actores.find(actor) != -1:
                    print(" "+Fore.YELLOW+impresion.nombre)
            print()
        elif opcion == "b":
            print()
            year = int(input(Fore.BLUE+"Año de estreno: "+Fore.WHITE))
            print()
            for impresion in movies:
                if impresion.año == year:
                    print(" "+Fore.YELLOW+impresion.nombre,Fore.BLACK+impresion.genero)
                    
        elif opcion == "c":
            print()
            genere = input(Fore.BLUE+"Género de la película: "+Fore.WHITE)
            print()
            for impresion in movies:
                var = impresion.genero.strip()
                if  var == genere or var == genere.capitalize() or var == genere.upper():
                    print("     "+Fore.YELLOW+impresion.nombre)
            print()
        else:
            print(Fore.RED+"La opción ingresada no es correcta.")
    elif option==4:
        print(Fore.RED+"Los colores deben ser ingresados en inglés, HEX o RGB.")
        color1 = input(Fore.BLUE+"De qué color desea ver las películas?     "+Fore.WHITE)
        color2 = input(Fore.BLUE+"De qué color desea ver a los actores?     "+Fore.WHITE)

        dot = graphviz.Digraph(comment="Example")
        indi = 0
        for movie in movies:
            indi=indi+1
            var1="a"+str(indi)
            dot.node(var1,movie.nombre+"\\n"+str(movie.año)+" | "+movie.genero,{"color":color1,"style":"filled","shape":"box"})
            print(var1)
            indi=indi+1
            var2="a"+str(indi)
            print(var2)
            dot.node(var2,movie.actores,{"color":color2,"style":"filled","shape":"box"})

            dot.edge(var1,var2)

        print(dot.source)
        r=open("Reportes/Report.txt","w")
        r.write(dot.source)
        r.close()
        os.system("dot -Tpng Reportes/Report.txt -o Reportes/Report.png")
        os.system("dot -Tpdf Reportes/Report.txt -o Reportes/Report.pdf")
        webbrowser.open_new_tab("C:/Users/sebas/Documents/USAC/Primer Semestre 2023/Lab LFP/Práctica 1/Reportes/Report.pdf")

    elif option == 5:
        print()
        print(Fore.RED+"¡Gracias por usar nuesto programa!")
        print(Fore.RED+" Esperamos verte de nuevo, pronto ")
        state = 1

root.mainloop()