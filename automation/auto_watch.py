import re

from bs4 import BeautifulSoup
from colorama import Fore

from settings import settings


class AutoWatcher(object):
    def __init__(self, session):
        self.session = session
        self.courses = None

    def get_all_courses(self, year="2018", semester="第一学期"):
        """
        为啥我不单独做个查询接口呢，因为，那个教务处查课程实在是太慢了
        :return:
        """
        data = settings.QUERY_CLASS['data']
        data['criteria'] = (data['criteria'] % (year, semester)).encode('gbk')
        settings.QUERY_CLASS['data'] = data

        response = self.session.post(**settings.QUERY_CLASS)
        raw_data = re.findall('trow\[\d+\] = "(.*)";', response.text)
        courses = dict()

        count = 0
        while True:
            raw_courses = raw_data[count: count + 15]
            if not len(raw_courses):
                break

            course = {
                "year": raw_courses[1],
                "semester": raw_courses[2],
                "class": raw_courses[3],
                "class_num": raw_courses[4],
                "class_id": re.findall('\\\\"(.*)\\\\"', raw_courses[5])[0],
                "class_name": re.findall("信息'>(.*)</font>", raw_courses[5])[0],
                "class_time": raw_courses[6],
                "teachers": raw_courses[7],
                "class_type": raw_courses[8],
                "class_hours": raw_courses[9],
                "class_score": raw_courses[10],
                "selected": raw_courses[13],
                "total": raw_courses[14]
            }

            courses[course['class_id']] = course
            count += 15

        self.courses = courses

        return courses

    def get_courses_by_params(self, **kwargs):
        """
        quick query
        :param kwargs: year, semester, class, class_num, class_id, class_name, class_time, teachers
                       class_hours, class_score, selected, total
        :return:
        """
        course_list = list()
        for course in self.courses.values():
            flag = False
            for key, value in kwargs.items():
                if value in course[key]:
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag:
                course_list.append(course)

        return course_list

    def crate_task_list(self):
        print(
            """
            example:
            class_name:分离
            class_num:1000120
            class_time:星期五
            class_teachers:小明
            ...
            很多参数，可以组合，不过这两三个就足够用了
            所有的参数都是包含匹配
            """
        )
        result_list = list()
        while True:
            filter_params = dict()
            print(Fore.LIGHTBLUE_EX + "=" * 40 + "\n")
            print(Fore.GREEN + "Please enter key:value as a filter: ")
            while True:
                param = input()
                if not param:
                    break
                key, value = param.split(":")
                filter_params[key] = value

            query_list = self.get_courses_by_params(**filter_params)
            for index, course in enumerate(query_list):
                print(str(index) + "    " + str(course))

            index = int(input("Please choose the course index to add, -1 to exit: "))

            if index == -1:
                break
            else:
                print("You have chosen: " + str(query_list[index]))
                result_list.append(query_list[index])

        print("Total courses: " + str(result_list))
        return result_list

    def get_students_of_course(self):
        """
        嗯，我就是犯懒了，这个接口格式化没写， 谁爱写谁写，偷偷告诉你，教务处前端还漏了初始化课程的接口
        :return:
        """
        print(
            """
            example:
            class_name:分离
            class_num:1000120
            class_time:星期五
            class_teachers:小明
            ...
            很多参数，可以组合，不过这两三个就足够用了
            所有的参数都是包含匹配
            """
        )
        filter_params = dict()
        print(Fore.LIGHTBLUE_EX + "=" * 40 + "\n")
        print(Fore.GREEN + "Please enter key:value as a filter: ")
        while True:
            param = input()
            if not param:
                break
            key, value = param.split(":")
            filter_params[key] = value

        print(filter_params)
        query_list = self.get_courses_by_params(**filter_params)
        for index, course in enumerate(query_list):
            print(str(index) + str(course))

        index = int(input("Please choose the course index to query, -1 to exit: "))
        if index == -1:
            return
        else:
            course = query_list[index]
            params = settings.QUERY_STUDENTS['params']
            params['id'] = course['class_id']

            response = self.session.get(**settings.QUERY_STUDENTS)
            soup = BeautifulSoup(response.text, features='lxml')
            result = soup.findAll('td', attrs={'align': 'left'})
            for item in result:
                temp = item.get_text().strip()
                if temp:
                    print(temp)
