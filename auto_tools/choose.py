import requests
from settings import settings
from bs4 import BeautifulSoup
import re
from urllib.parse import quote


def login():
    """
    login into grd.bit.edu.cn
    :return: True or False
    """
    session = requests.Session()
    response = session.get(url=settings.LOGIN['url'], params=settings.LOGIN['params'])
    soup = BeautifulSoup(response.text, features='lxml')
    post_params = soup.findAll('input', type='hidden')
    for param in post_params:
        settings.LOGIN['data'].update(
            {
                param.attrs['name']: param.attrs['value']
            }
        )
    response = session.post(**settings.LOGIN)
    return session


def get_courses(session):
    response = session.post(**settings.QUERY_CLASS)
    raw_data = re.findall('trow\[\d+\] = "(.*)";', response.text)
    result_data = dict()

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
            "class_type": temp_course[8],
            "class_hours": temp_course[9],
            "class_score": temp_course[10],
            "selected": temp_course[13],
            "total": temp_course[14]
        }
        result_data[course['class_id']] = course
        count += 15

    return result_data


def get_course_students(session, class_id):
    settings.QUERY_STUDENTS['params']['id'] = class_id
    response = session.get(**settings.QUERY_STUDENTS)
    soup = BeautifulSoup(response.text, features="lxml")
    raw_data = soup.findAll('td', attrs={"align": "left"})
    result_data = list()

    count = 0
    while True:
        temp_student = raw_data[count: count + 7]
        if not len(temp_student):
            break

        student = {
            "student_name": temp_student[1].get_text(strip=True),
            "student_academy": temp_student[2].get_text(strip=True),
            "student_pro": temp_student[3].get_text(strip=True),
            "student_degree": temp_student[6].get_text(strip=True)
        }
        result_data.append(student)
        count += 7

    return result_data


def get_select_course_page(session):
    response = session.get(**settings.GET_COURSES)
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
    print(params)
    print(data)
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
    data['c0-e13'] = 'string:' + params['kkxn']# 课程学年
    data['c0-e14'] = 'string:' + quote(params['kkxq'])# 课程学期
    data['c0-e15'] = 'string:' + '402848c064580bb0016458a0dc4c0230'
    data['c0-e16'] = 'string:' + '1700001'
    data['c0-e17'] = 'string:' + '%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90' #课程名称
    data['c0-e18'] = 'string:' + ''
    data['c0-e19'] = 'string:' + '%E4%B8%93%E4%B8%9A%E5%BF%85%E4%BF%AE%E8%AF%BE' # 课程类型
    data['c0-e20'] = 'string:' + '%E4%B8%93%E4%B8%9A%E5%BF%85%E4%BF%AE%E8%AF%BE'
    data['c0-e21'] = 'string:' + '32'
    data['c0-e22'] = 'string:' + '2'
    data['c0-e23'] = 'string:' + ''

    settings.SELECT_COURSE['data'] = data
    print(data)


def select_course(session):
    response = session.post(**settings.SELECT_COURSE)
    print(response.request.body)
    print(response.text)