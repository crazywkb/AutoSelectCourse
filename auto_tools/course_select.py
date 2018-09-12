from settings import settings
import requests
from settings import settings
from bs4 import BeautifulSoup
import re
from urllib.parse import quote


class CourseSelect(object):
    def __init__(self):
        self.courses = dict()
        self.task_list = list()
        self.session = requests.Session()
        self.__login()

    def __login(self):
        response = self.session.get(url=settings.LOGIN['url'], params=settings.LOGIN['params'])
        soup = BeautifulSoup(response.text, features='lxml')
        post_params = soup.findAll('input', type='hidden')
        for param in post_params:
            settings.LOGIN['data'].update(
                {
                    param.attrs['name']: param.attrs['value']
                }
            )
        self.session.post(**settings.LOGIN)

    def get_courses(self):
        response = self.session.post(**settings.QUERY_CLASS)
        raw_data = re.findall('trow\[\d+\] = "(.*)";', response.text)
        result_data = self.courses

        count = 0
        while True:
            temp_course = raw_data[count: count + 15]
            if not len(temp_course):
                break

            course = {
                "year": temp_course[1],
                "semester": temp_course[2],
                "class": temp_course[3],
                "class_num": temp_course[4],
                "class_id": re.findall('\\\\"(.*)\\\\"', temp_course[5])[0],
                "class_name": re.findall("信息'>(.*)</font>", temp_course[5])[0],
                "class_time": temp_course[6],
                "teachers": temp_course[7],
                "class_hours": temp_course[9],
                "class_score": temp_course[10],
                "selected": temp_course[13],
                "total": temp_course[14]
            }
            result_data[course['class_id']] = course
            count += 15

    def get_necessary_params(self):
        response = self.session.get(**settings.GET_COURSES)
        soup = BeautifulSoup(response.text, features="lxml")
        input_params = soup.findAll('input', type='hidden')
        params = dict()
        for param in input_params:
            params.update(
                {
                    param.attrs.get('name', 'None'): param.attrs.get('value', 'None')
                }
            )
        data = settings.SELECT_COURSE['data']
        data['c0-e1'] = 'string:' + params['xh']
        data['c0-e2'] = 'string:' + params['lb']
        data['c0-e3'] = 'string:' + params['studentId']
        data['c0-e4'] = data['c0-e3']
        data['c0-e5'] = 'string:' + quote(params['pycc'])
        data['c0-e6'] = 'string:' + quote(params['xslb'])
        data['c0-e7'] = 'string:' + params['nj']
        data['c0-e8'] = 'string:' + quote(params['ldfs'])
        data['c0-e9'] = 'string:' + params['ptlx']
        data['c0-e10'] = 'string:' + params['studentId']
        data['c0-e11'] = 'string:' + params['xh']
        data['c0-e12'] = 'string:' + params['lb']
        data['c0-e13'] = 'string:' + params['kkxn']  # 课程学年
        data['c0-e14'] = 'string:' + quote(params['kkxq'])  # 课程学期
        settings.SELECT_COURSE['data'] = data

    def post_data_format(self, course):
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
        return data

    def entry(self):
        print("Start to crawl the courses...")
        self.get_courses()
        print("Courses have been crawled and saved...")

        print("=" * 30)

        print("Please choose operation: ")
        print("1. add course")
        print("2. delete course")
        print("3. run")

        operations = {
            '1': self.add_course,
            '2': self.delete_course,
            '3': self.run
        }

        while True:
            operation = input()
            operations[operation]()

    def add_course(self):
        course_id = input("Please enter course_id: ")
        course = self.courses.get(course_id, default=None)
        if not course:
            print("Course doesn't exist.")
        else:
            self.task_list.append(self.post_data_format(course))

    def delete_course(self):
        course_id = input("Please enter course_id to del: ")
        course = self.courses.get(course_id, default=None)
        if not course:
            print("Course doesn't exist in task list.")
        else:
            self.task_list.remove(self.post_data_format(course))

    def run(self):
        pass


if __name__ == '__main__':
    course_selector = CourseSelect()
    course_selector.entry()
