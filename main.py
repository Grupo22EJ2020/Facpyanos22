from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')
#from curso import Curso
#from empleado import Empleado
#from video import Video
#from tema import Tema
from curso_tema import Curso_Tema
from curso_tema_video import Curso_Tema_Video
while True:
    limpiar_pantalla()
    try:
        opcion=int(input("¿Donde desea interactuar?\n1)Empleados\n2)Curso\n3)Temas\n4)Videos\n5)Temas Asignados\n6)VideosAsignados\n7)Salir\n8)Opcion: "))
        if opcion<1:
            input("Error, introduzca un numero valido, enter para continuar... ")
        elif opcion==1:
            pass
#            valor=Curso(None,None,None)
#            valor.Minimenu()
        elif opcion==2:
            pass
#           valor=Empleado(None,None,None)
#           valor.Minimenu()
        elif opcion==3:
            pass
#           valor=Video(None,None,None)
#           valor.Minimenu()
        elif opcion==4:
            pass
#           valor=Tema(None,None,None)
#           valor.Minimenu()
        elif opcion==5:
            valor=Curso_Tema(0,0,0)
            valor.Minimenu()
        elif opcion==6:
            valor=Curso_Tema_Video(0,0,0)
            valor.Minimenu()
        elif opcion==7:
            limpiar_pantalla()
            break
        elif opcion>7:
            input("Error, introduzca un numero valido, enter para continuar...")
    except ValueError:
        limpiar_pantalla()
        input("Error, introducir unicamente numero, vuelva a intentar, enter para continuar...")
            
            
