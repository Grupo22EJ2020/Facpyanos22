class Aplicacion:
    def __init__(self,idEmpleado,nombre,direccion):
        self.__idEmpleado= idEmpleado
        self.__nombre= nombre
        self.__direccion= direccion
    
    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevonombre):
        self.__nombre= nuevonombre

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self,nuevadireccion):
        self.__direccion= nuevadireccion
    def __eq__(self,valor):
        return self.__idEmpleado==valor.__idEmpleado


    def minimenu (self):

        empleados = []
        while True:
            print ("\n1. Agregar empleado\n2.Borrar empleado\n3.Modificar empleado\n4. Ver detalles de empleado\n5.Salir")

            accion= int(input("¿Que accion desea ejecutar:"))
            if accion ==1:

                self.__idEmpleado= self.__idEmpleado+1
                self.__nombre=input("Dame el nombre del empleado: ")
                self.__direccion=input("Dame la direccion del empleado")
                datos=Aplicacion(self.__idEmpleado,self.__nombre,self.__direccion)
                empleados.append(datos)
       
            elif accion ==2:
                if empleados==[]:
                    input("Actualmente vacia, enter para continuar...")
                else:
                    clave=int(input("Clave:"))
                    for remover in empleados:
                        if remover.idEmpleado == clave:
                            empleados.remove(Aplicacion(clave,None,None))
                            input("Registro borrado")
            elif accion ==3:
                clave=int(input("Clave:"))
                if empleados==[]:
                    input("Registro vacio actualmente")
                else:
                    for remover in empleados:
                        if remover.idEmpleado==clave:
                            remover.nombre=input("Dame el nombre nuevo del empleado: ")
                            remover.direccion=input("Dame la direccion nueva: ")
                            input("Registro Actualizado")
            elif accion==4:
                if empleados==[]:
                    input("Registro vacio actualmente")
                else:
                    print(f"{'idEmpleado':<20}{'nombre':<20}{'direccion':<20}")

                    for posicion in empleados:
                        print(f"{posicion.idEmpleado:<20}{posicion.nombre:<20}{posicion.direccion:<20}")
            elif accion == 5:
                break 
            elif accion>5:
                input("Error, introduzca numero del minimenu")

            def guardado():
                archivo=open("./archivos/Empleado.txt","w")
                for posicion in empleados:
                    archivo.write(str(f" idEmpleado: {posicion.idEmpleado}, nombre: {posicion.nombre}, direccion: {posicion.direccion} ""\n"))
                archivo.close()
            guardado()