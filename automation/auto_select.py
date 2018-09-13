import random
import re
import time
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup
from colorama import Fore

from settings import settings


class AutoSelect(object):
    def __init__(self, session, course_list):
        self.session = session
        self.course_list = course_list
        self.data_list = list()

    def __get_necessary_data(self):
        response = self.session.get(**settings.GET_COURSES)
        soup = BeautifulSoup(response.text, features="lxml")
        raw_data = soup.findAll('input', type='hidden')
        necessary_data = dict()
        for param in raw_data:
            necessary_data.update(
                {
                    param.attrs.get('name', 'None'): param.attrs.get('value', 'None')
                }
            )

        response = self.session.get(**settings.GET_ENGINE_JS)

        script_session_id = re.search('dwr.engine._origScriptSessionId = "(.*)";', response.text)[0]
        script_session_id = script_session_id + str(int(random.random() * 1000))
        http_session_id = self.session.cookies.get("JSESSIONID", domain='grdms.bit.edu.cn/yjs', default=None)

        data = settings.SELECT_COURSE['data']
        data['httpSessionId'] = http_session_id
        data['scriptSessionId'] = script_session_id
        data['c0-e1'] = 'string:' + necessary_data['xh']
        data['c0-e2'] = 'string:' + necessary_data['lb']
        data['c0-e3'] = 'string:' + necessary_data['studentId']
        data['c0-e4'] = data['c0-e3']
        data['c0-e5'] = 'string:' + quote(necessary_data['pycc'])
        data['c0-e6'] = 'string:' + quote(necessary_data['xslb'])
        data['c0-e7'] = 'string:' + necessary_data['nj']
        data['c0-e8'] = 'string:' + quote(necessary_data['ldfs'])
        data['c0-e9'] = 'string:' + necessary_data['ptlx']
        data['c0-e10'] = 'string:' + necessary_data['studentId']
        data['c0-e11'] = 'string:' + necessary_data['xh']
        data['c0-e12'] = 'string:' + necessary_data['lb']
        data['c0-e13'] = 'string:' + necessary_data['kkxn']  # 课程学年
        data['c0-e14'] = 'string:' + quote(necessary_data['kkxq'])  # 课程学期
        settings.SELECT_COURSE['data'] = data

    def __generate_post_data_list(self):
        for course in self.course_list:
            data = settings.SELECT_COURSE['data'].copy()
            data['c0-e15'] = 'string:' + course['class_id']
            data['c0-e16'] = 'string:' + course['class_num']
            data['c0-e17'] = 'string:' + quote(course['class_name'])  # 课程名称
            data['c0-e18'] = 'string:' + ''
            data['c0-e19'] = 'string:' + quote(course['class_type'])  # 课程类型
            data['c0-e20'] = 'string:' + quote(course['class_type'])
            data['c0-e21'] = 'string:' + quote(course['class_hours'])
            data['c0-e22'] = 'string:' + quote(course['class_score'])
            data['c0-e23'] = 'string:' + ''
            self.data_list.append(data)

    def run_and_wait(self):
        self.__get_necessary_data()
        self.__generate_post_data_list()
        limit = int(input("How many times the requests will post per second(1-40): "))

        if limit < 1 or limit > 40:
            print("Error input.")
            return 0

        print(Fore.LIGHTBLUE_EX + "Running crazyly ......")
        while len(self.data_list):
            data_list = list()
            time.sleep(1 / limit)
            for data in self.data_list:
                response = self.session.post(url=settings.SELECT_COURSE['url'], data=data)
                if 'success' in response.text:
                    print(Fore.RED + unquote(data['c0-e17']) + "    success.")
                elif 'failure' in response.text:
                    reason = re.findall('\["failure","(.*)"\]', response.text)[0].encode("utf-8").decode(
                        'unicode_escape')
                    if "超过限选人数" in reason:
                        data_list.append(data)
                    else:
                        print(Fore.RED + reason)
                        print("This course has been removed from task list.")
            self.data_list = data_list
