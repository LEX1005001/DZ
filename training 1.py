from random import randint
class Camera:
    def __init__(self,name) -> None:
        self.name=name
        self.snapshots=0
        self.album=[]
    def take_photo(self):
        self.snapshots+=1
        self.album.append(1==randint(0,1))
    def info(self):
        print(f"Название камеры <{self.name}>\nКол-во снимков <{self.snapshots}>\nАльбом фотографий->{self.album}")
cam1=Camera("Rock")
cam1.take_photo()
cam1.take_photo()
cam1.take_photo()
cam1.info()