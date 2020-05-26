from os import system,name
def limpiar_pantalla():
    if name=='nt':
        system('cls')
    else:
        system('clear')
class Curso_Tema_Video:
    def __init__(self, idCursoTV,idCT,idVideo):
        self.__icttv=idCursoTV
        self.__ict=idCT
        self.__iv=idVideo
    @property
    def icttv(self):
        return self.__icttv
    @property
    def ict(self):
        return self.__ict
    @ict.setter
    def ict(self,valor):
        self.__ict=valor
    @property
    def iv(self):
        return self.__iv
    @iv.setter
    def iv(self,valor):
        self.__iv=valor
    def __eq__(self,otro):
        return self.__icttv == otro.__icttv
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
                    idctema=open("./archivos/Curso_Tema.txt","r")
                    print(idctema.read())
                    input("Base de datos Actual, enter para continuar...")
                    idctema.close()
                    self.__ict=int(input("Dame el idCursoTema: "))
                    limpiar_pantalla()
                    videoid=open("./archivos/VIDEO.txt","r")
                    print(videoid.read())
                    input("Base de datos Actual, enter para continuar...")
                    videoid.close()
                    self.__iv=int(input("Dame el idvideo: "))
                    self.__icttv=self.__icttv+1
                    valores=Curso_Tema_Video(self.__icttv,self.__ict,self.__iv)
                    lista.append(valores)
                    input("Registro Agregado, enter para continuar...")
                    limpiar_pantalla()
                elif opcion==2:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i1 in lista:
                        print(f"{i1.icttv:<30}{i1.ict:<30}{i1.iv:<30}")
                    if lista==[]:
                        input("Actualmente vacia, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        clave=int(input("Clave:"))
                        for remover in lista:
                            if remover.icttv == clave:
                                lista.remove(Curso_Tema_Video(clave,None,None))
                                input("Registro borrado, enter para continuar...")
                                limpiar_pantalla()
                elif opcion==3:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i2 in lista:
                        print(f"{i2.icttv:<30}{i2.ict:<30}{i2.iv:<30}")
                    clave=int(input("Clave:"))
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        for remover in lista:
                            if remover.icttv==clave:
                                remover.ict=int(input("Dame el idCT nuevo: "))
                                remover.iv=int(input("Dame el idvideo nuevo: "))
                                input("Registro Actualizado, enter para continuar...")
                            limpiar_pantalla()
                elif opcion==4:
                    limpiar_pantalla()
                    if lista==[]:
                        input("Registro vacio actualmente, enter para continuar...")
                        limpiar_pantalla()
                    else:
                        print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                        for i3 in lista:
                            print(f"{i3.icttv:<30}{i3.ict:<30}{i3.iv:<30}")
                        input("Enter para continuar...")
                        limpiar_pantalla()
                elif opcion==5:
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i4 in lista:
                        print(f"{i4.icttv:<30}{i4.ict:<30}{i4.iv:<30}")
                    clave=int(input("Clave:"))
                    limpiar_pantalla()
                    print(f"\n{'idCursoTV':<30}{'idCT':<30}{'idVideo':<30}")
                    for i5 in lista:
                        if i5.icttv==clave:
                            print(f"{i5.icttv:<30}{i5.ict:<30}{i5.iv:<30}")
                    input("Enter para continuar...")
                elif opcion==6:
                    break
                elif opcion>6:
                    input("Error, introduzca numero correcto, enter para continuar...")
                    limpiar_pantalla()
                def informacion():
                    archivo=open("./archivos/Curso_Tema_Video.txt","w")
                    for i6 in lista:
                        archivo.write(str(f" IdCursoTV: {i6.icttv}, IdCT: {i6.ict}, IdVideo: {i6.iv}""\n"))
                    archivo.close()
                informacion()
                limpiar_pantalla()
            except ValueError:
                limpiar_pantalla()
                input("Error, introducir unicamente numero, vuelva a intentar, enter para continuar...")
            