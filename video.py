class Video:
    def _init_ (self,idVideo,nombre,url,fechapublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__fechapublicacion = int(fechapublicacion)
        self.__url = url
       
    @property
    def idVideo(self):
        return self.__idVideo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevonombre):
        self.__nombre = nuevonombre
    @property
    def fechapublicacion(self):
        return self.__fechapublicacion
    @fechapublicacion.setter
    def fechapublicacion(self,nuevafecha):
        self.__fechapublicacion = int(nuevafecha)
    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self,nuevourl):
        self.__url = nuevourl
       
    def _str_ (self):
        return self.__nombre
    def datos(self):
        return f"Es un video con la clave:{self.__idVideo},nombre del video:{self.__nombre},con fecha de publicacion de:{self.__fechapublicacion} y su URL es {self.__url}"
   
    def agregarVideo(idVideo,nombre,fechapublicacion,url,lista):
        video = idVideo
        video = Video(idVideo,nombre,fechapublicacion,url)
        lista.append(video)
        print("Video agregado!")
    def verLista(lista):
        print("La lista de videos es:\n")
        for video in lista:
            print(video.idVideo)
    def modificarnombre(self,clave):
        nuevonombre = input("Cual nombre le quieres poner?")
        clave.nombre = nuevonombre
    def modificarfecha(self,clave):
        nuevafecha = int(input("Que fecha le quieres poner?"))
        clave.nuevafecha = int(nuevafecha)
    def modificarURL(self,clave):
        nuevourl = input("Por cual URL la quieres modificar?")
        clave.url = nuevourl
    def eliminarVideo(lista):
        videoelim = input("Escriba la clave del video que desee eliminar: ")
        for video in lista:
            if video == videoelim:
                lista.remove(video)
                print("Su video ha sido removido.")
list = []
video1 = Video("1121", "python", "0", 51220)
list.append(video1)
menuOpciones = "1.- Ver info de todos los videos.\n2.- Elegir un video.\n3.- Agregar un video.\n4.- Eliminar un video.\n5.- Modificar los datos de un video.\n6.- Salir"    
submenuOpciones = "1.- Ver datos del video."
Minimenu = 0

Video.verLista(list)
clave = input("Cual es la id de tu video?: ")
for video in list:
    if clave == video.idVideo:
        print(submenuOpciones)
        submenu = input("Que desea hacer?: ")
        if submenu == "1":
            print(video.datos())

   
print(menuOpciones)
Minimenu = int(input("Que desea hacer?: "))
while Minimenu != 6:
    if Minimenu == 1:
        Video.verLista(list)
        print(menuOpciones)
        Minimenu = int(input("Que desea hacer?: "))
    if Minimenu == 2:
        Video.verLista(list)
        clave = input("Cual es la id de tu video?: ")
        for video in list:
            if clave == video.idVideo:
                print(submenuOpciones)
                submenu = input("Que desea hacer?: ")
                if submenu == "1":
                    print(video.datos)
        print(menuOpciones)
        Minimenu = int(input("Que desea hacer?: "))
    if Minimenu == 3:
        idVideo = input("Dame la id del video: ")
        nombre = input("Dame el nombre del video: ")
        fechapublicacion = input("Dame la fecha del video: ")
        url = input("Dame el url del video: ")
        Video.agregarVideo(idVideo,nombre,fechapublicacion,url,list)
        print(menuOpciones)
        Minimenu = int(input("Que desea hacer?: "))
    if Minimenu == 4:
        Video.eliminarVideo(list)
        print(menuOpciones)
        Minimenu = int(input("Que desea hacer?: "))
    if Minimenu == 5:
        Video.verLista
        clave = input("Cual es la clave del video que desea modificar?:")
        for video in list:
            if clave == video.idVideo:
                submenu == input("Quieres cambiarle el nombre, la fecha o el url?")
                if submenu == "titulo":
                    video.modificarnombre(video)
                elif submenu == "fechapublicacion":
                    video.modificarfecha(video)
                elif submenu == "url":
                    video.modificarURL(video)
        print(menuOpciones)
        Minimenu = int(input("Que desea hacer?: "))
print("El programa ha concluido con éxito")
