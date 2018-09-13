import requests
from bs4 import BeautifulSoup
from settings import settings
from colorama import Fore, init
init()


class AutoLogin(object):
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__necessary_params = None
        self.session = requests.Session()
        self.__data = dict()

    def __get_user_info(self):
        print(Fore.LIGHTBLUE_EX + "="*40)
        self.__username = input("Please enter username: ")
        self.__password = input("Please enter password: ")

    def __get_necessary_params(self):
        response = self.session.get(url=settings.LOGIN['url'], params=settings.LOGIN['params'])
        soup = BeautifulSoup(response.text, features='lxml')
        raw_data = soup.findAll('input', type='hidden')

        for param in raw_data:
            self.__data.update(
                {
                    param.attrs['name']: param.attrs['value']
                }
            )

        self.__data.update(
            {
                'username': self.__username,
                'password': self.__password
            }
        )

    def login(self):
        self.__get_user_info()
        self.__get_necessary_params()

        response = self.session.post(data=self.__data, **settings.LOGIN)
        assert response.status_code == 200
        print(Fore.BLUE + "Login successfully.")


if __name__ == '__main__':
    login = AutoLogin()
    login.login()
