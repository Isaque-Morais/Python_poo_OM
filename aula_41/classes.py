class Writer:
    def __init__(self, name):
        self.__name = name
        self.__tool = None
    
    #Getter
    @property
    def name(self):
        return self.__name

    #Setter
    @property
    def tool(self):
        return self.__tool
    
    @tool.setter
    def tool(self, tool):
        self.__tool = tool

class Pen:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def write(self):
        print('Caneta está escrevendo...')

class Typewriter:
        def write(self):
            print('A máquina está escrevendo...')