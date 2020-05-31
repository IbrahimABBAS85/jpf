
class SettingElement(object):
    """description of class"""
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
       self.__name = value
   
    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, value):
       self.__isActive = value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
       self.__value = value
    
    def __init__(self, name, value, active):
        self.name = name
        self.value = value
        self.active = active
