from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')
class Curso_Tema:
    def __init__(self, idCursoTema,idCurso,idTema):
        self.__ict=idCursoTema
        self.__ic=idCurso
        self.__it=idTema
    @property
    def ict(self):
        return self.__ict
    @property
    def ic(self):
        return self.__ic
    @ic.setter
    def ic(self,valor):
        self.__ic=valor
    @property
    def it(self):
        return self.__it
    @it.setter
    def it(self,valor):
        self.__it=valor
    def __eq__(self,otro):
        return self.__ict == otro.__ict
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
                    curso=open("./archivos/curso.txt","r")
                    print(curso.read())
                    input("Base de Datos Actual,Enter para continuar...")
                    curso.close()
                    self.__ic=int(input("Dame el curso: "))
                    limpiar_pantalla()
                    tema=open("./archivos/Tema.txt","r")
                    print(tema.read())
                    input("Base de Datos Actual,Enter para continuar...")
                    tema.close()
                    self.__it=int(input("Dame el tema: "))
                    limpiar_pantalla()
                    self.__ict=self.__ict+1
                    valores=Curso_Tema(self.__ict,self.__ic,self.__it)
                    lista.append(valores)
                    input("Registro Agregado, enter para continuar...")
                    limpiar_pantalla()
                elif opcion==2:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i1 in lista:
                        print(f"{i1.ict:<30}{i1.ic:<30}{i1.it:<30}")
                    if lista==[]:
                        input("Actualmente vacia, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        clave=int(input("Clave:"))
                        for remover in lista:
                            if remover.ict == clave:
                                lista.remove(Curso_Tema(clave,None,None))
                                input("Registro borrado, enter para continuar...")
                                limpiar_pantalla()
                elif opcion==3:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i2 in lista:
                        print(f"{i2.ict:<30}{i2.ic:<30}{i2.it:<30}")
                    clave=int(input("Clave:"))
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        for remover in lista:
                            if remover.ict==clave:
                                remover.ic=int(input("Dame el curso nuevo: "))
                                remover.it=int(input("Dame el tema nuevo: "))
                                input("Registro Actualizado, enter para continuar...")
                            limpiar_pantalla()
                elif opcion==4:
                    limpiar_pantalla()
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                        for i3 in lista:
                            print(f"{i3.ict:<30}{i3.ic:<30}{i3.it:<30}")
                        input("Enter para continuar...")
                        limpiar_pantalla()
                elif opcion==5:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i4 in lista:
                        print(f"{i4.ict:<30}{i4.ic:<30}{i4.it:<30}")
                    clave=int(input("Clave:"))
                    limpiar_pantalla()
                    print(f"\n{'idCursoTema':<30}{'idCurso':<30}{'idTema':<30}")
                    for i5 in lista:
                        if i5.ict==clave:
                            print(f"{i5.ict:<30}{i5.ic:<30}{i5.it:<30}")
                    input("Enter para continuar...")
                elif opcion==6:
                    break
                elif opcion>6:
                    input("Error, introduzca numero correcto, enter para continuar...")
                    limpiar_pantalla()
                def informacion():
                    archivo=open("./archivos/Curso_Tema.txt","w")
                    for i6 in lista:
                        archivo.write(str(f" IdCursoTema: {i6.ict}, IdCurso: {i6.ic}, IdTema: {i6.it}""\n"))
                    archivo.close()
                informacion()
            except ValueError:
                limpiar_pantalla()
                input("Error, introducir unicamente numero, vuelva a intentar, enter para continuar...")
            
