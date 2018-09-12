import requests
from settings import settings
from colorama import Fore


class AutoLogin(object):
    def __init__(self):
        self.username = None
        self.password = None
        self.necessary_params = None

    def __get_user_info(self):
        self.username = input(Fore.GREEN + "Please enter username: ")
        self.password = input(Fore.GREEN + "Please enter password: ")

    def __get_necessary_params(self):
        pass

    def login(self):
        self.__get_user_info()
        self.__get_necessary_params()


if __name__ == '__main__':
    pass