class Camera:
    def __init__(self, name = 'Alpha', memory = '4000mb', zoom = '1,5x', num = 1234, model = 'Sigma'):
        self.__name = name
        self.__memory = memory
        self.__zoom = zoom
        self.number = num
        self.model = model

    def get_name(self):
        return self.__name

    def get_memory(self):
        return self.__memory

    def get_zoom(self):
        return self.__zoom
#для рядків
    def __str__(self):
        return f'Виробник: {self.__name}, Ємність: {self.__memory}, Кратність зуму: {self.__zoom}, Серія: {self.number}, Модель: {self.model}'

    def __repr__(self):
        return f'Camera({self.__name}, {self.__memory}, {self.__zoom}, {self.number}, {self.model})'

    def __del__(self):
        print(f'Об`єкт {self.__name} не існує')

def main():
    camera = Camera()
    camera1 = Camera('GoPro', '12000mb', '2x', 1161, 'Lilium')
    camera2 = Camera('NikePro', '15000mb', '5x', 1277, 'Shenn')

    print(camera)
    print(camera1)
    print(camera2)

    print(f'{camera.get_name()}, {camera.get_memory()}, {camera.get_zoom()}')
    print(f'{camera1.get_name()}, {camera1.get_memory()}, {camera1.get_zoom()}')
    print(f'{camera2.get_name()}, {camera2.get_memory()}, {camera2.get_zoom()}')

    camera.__repr__()

main()