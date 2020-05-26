from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')
class Cursoo:
    def __init__(self, idCurso,descripcion,idEmpleado):
        self.__idCurso=idCurso
        self.__descripcion=descripcion
        self.__idEmpleado=idEmpleado
    @property
    def idCurso(self):
        return self.__idCurso
    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self,contenido):
        self.__descripcion=contenido
    @property
    def idEmpleado(self):
        return self.__idEmpleado
    @idEmpleado.setter
    def idEmpleado(self,codigo):
        self.__idEmpleado=codigo
    def __eq__(self,otro):
        return self.__idCurso == otro.__idCurso
    def Minimenu(self):
        limpiar_pantalla()
        lista=[]
        while True:
            try:
                opcion=int(input("¿Qué Desea hacer?\n1)Agregar\n2)Borrar\n3)Modificar\n4)Consultar\n5)Elegir Clave\n6)Salir\nOpcion:"))
                if opcion<1:
                    limpiar_pantalla()
                    input("Error, introduzca numero correcto, enter para continuar...")
                elif opcion==1:
                    limpiar_pantalla()
                    self.__descripcion=int(input("Dame la descripcion: "))
                    self.__idEmpleado=int(input("Dame el codigo del empleado: "))
                    self.__idCurso=self.__idCurso+1
                    valores=Cursoo(self.__idCurso,self.__idCurso,self.__descripcion)
                    lista.append(valores)
                    input("Registro Agregado, enter para continuar...")
                    limpiar_pantalla()
                elif opcion==2:
                    limpiar_pantalla()
                    print(f"\n{'idCurso':<30}{'descripcion':<30}{'idEmpleado':<30}")
                    for i1 in lista:
                        print(f"{i1.idCurso:<30}{i1.descripcion:<30}{i1.idEmpleado:<30}")
                    if lista==[]:
                        input("Actualmente vacia, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        clave=int(input("Clave:"))
                        for remover in lista:
                            if remover.idCurso == clave:
                                lista.remove(Cursoo(clave,None,None))
                                input("Registro borrado, enter para continuar...")
                                limpiar_pantalla()
                elif opcion==3:
                    limpiar_pantalla()
                    print(f"\n{'idCurso':<30}{'descripcion':<30}{'idEmpleado':<30}")
                    for i2 in lista:
                        print(f"{i2.idCurso:<30}{i2.descripcion:<30}{i2.idEmpleado:<30}")
                    clave=int(input("Clave:"))
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        for remover in lista:
                            if remover.idCurso==clave:
                                remover.descripcion=int(input("Dame la descripcion nueva: "))
                                remover.idEmpleado=int(input("Dame el codigo del empleado nuevo: "))
                                input("Registro Actualizado, enter para continuar...")
                            limpiar_pantalla()
                elif opcion==4:
                    limpiar_pantalla()
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        print(f"\n{'idCurso':<30}{'descripcion':<30}{'idEmpleado':<30}")
                        for i3 in lista:
                            print(f"{i3.idCurso:<30}{i3.descripcion:<30}{i3.idEmpleado:<30}")
                        input("Enter para continuar...")
                        limpiar_pantalla()
                elif opcion==5:
                    limpiar_pantalla()
                    print(f"\n{'idCurso':<30}{'descripcion':<30}{'idEmpleado':<30}")
                    for i4 in lista:
                        print(f"{i4.idCurso:<30}{i4.descripcion:<30}{i4.idEmpleado:<30}")
                    clave=int(input("Clave:"))
                    limpiar_pantalla()
                    print(f"\n{'idCurso':<30}{'descripcion':<30}{'idEmpleado':<30}")
                    for i5 in lista:
                        if i5.idCcursot==clave:
                            print(f"{i5.idCurso:<30}{i5.descripcion:<30}{i5.idEmpleado:<30}")
                    input("Enter para continuar...")
                elif opcion==6:
                    break
                elif opcion>6:
                    input("Error, introduzca numero correcto, enter para continuar...")
                    limpiar_pantalla()
                def informacion():
                    archivo=open("./archivos/curso.txt","w")
                    for i6 in lista:
                        archivo.write(str(f" IdCurso: {i6.idCurso}, descripcion: {i6.descripcion}, IdEmpleado: {i6.idEmpleado} |-| "))
                    archivo.close()
                informacion()
            except ValueError:
                limpiar_pantalla()
                input("Error, introducir unicamente numero, vuelva a intentar, enter para continuar...")