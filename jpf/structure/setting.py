

class Setting(object):
    """description of class"""

    @property
    def setting_option(self):
        return self.__setting_option
    @setting_option.setter
    def setting_option(self, value):
       self.__setting_option = value

    @property
    def is_instant_saving(self):
        return self.__is_instant_saving
    @is_instant_saving.setter
    def is_instant_saving(self, value):
       self.__is_instant_saving = value

    def __init__(self, setting_option = None, is_instant_saving = None):
        self.__setting_option = setting_option
        self.__is_instant_saving = is_instant_saving

