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
                