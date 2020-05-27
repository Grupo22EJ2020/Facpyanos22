class Tema:
    def __init__(self,idTema,nombre):
        self.__idTema= idTema
        self.__nombre= nombre
        
    
    @property
    def idTema(self):
        return self.__idTema

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevonombre):
        self.__nombre= nuevonombre
    def __eq__(self,otro):
        return self.__idTema==otro.__idTema

    def minimenu (self):

        tema = []
        while True:
            print ("\n1. Agregar empleado\n2.Borrar empleado\n3.Modificar empleado\n4. Ver detalles de empleado\n5.Salir")

            accion= int(input("¿Cual es la accion que desea ejecutar?:"))
            if accion ==1:

                self.__idTema= self.__idTema+1
                self.__nombre=input("Introduzca el nombre del empleado: ")
                datos=Tema(self.__idTema,self.__nombre)
                tema.append(datos)

            elif accion ==2:
                if tema==[]:
                    input("Actualmente se encuentra vacia, presione enter para continuar...")
                else:
                    clave=int(input("Clave:"))
                    for remover in tema:
                        if remover.idTema == clave:
                            tema.remove(Tema(clave,None))
                            input("El registro fue borrado")

            elif accion ==3:
                clave=int(input("Clave:"))
                if tema==[]:
                    input("El registro esta vacio actualmente")
                else:
                    for remover in tema:
                        if remover.idTema==clave:
                            remover.nombre=input("Introduzca el nombre nuevo del empleado: ")
                            input("El registro fue actualizado con exito")            

            elif accion ==4:
                if tema==[]:
                    input("El registro esta vacio actualmente")
                else:
                    print(f"{'idTema':<20}{'nombre':<20}")

                    for posicion in tema:
                        print(f"{posicion.idTema:<20}{posicion.nombre:<20}")

            elif accion ==5:
                break 
            elif accion>5:
                input("Error, introduzca numero del minimenu")

            def guardado():
                archivo=open("./archivos/Tema.txt","w")
                for posicion in tema:
                    archivo.write(str(f" idTema: {posicion.idTema}, nombre: {posicion.nombre} ""\n"))
                archivo.close()
            guardado()