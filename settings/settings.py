USERNAME = "2220170618"
PASSWORD = "300014"

LOGIN = {
    'url': 'https://login.bit.edu.cn/cas/login',
    'params': {
        'service': 'http://grdms.bit.edu.cn/yjs/login_cas.jsp'
    },
    'data': {
        'username': USERNAME,
        'password': PASSWORD
    }
}

QUERY_CLASS = {
    'url': 'http://grdms.bit.edu.cn/yjs/yanyuan/py/pyjxjhQuery.do',
    'params': {
        'method': 'query',
        'index': 'end',
        'pager.offset': "0",
    },
    'data': {
        "criteria": "kkxn = '2018' and kkxq = '第一学期'".encode('gbk'),
        "maxPageItems": "2000",
        "maxIndexPages": "5",
        "defName": "pyjxjhStuQuery",
        "defaultcriteria": " 1=1 ",
        "orderby2": " kkxn,kkxq,kcdm,jxbmc asc ".encode('gbk'),
        "hiddenColumns": "null",
        "pager.offset": "0",
        "maxPageItemsSelect": "2000",
        "maxPageItems2": "2000"
    }
}

QUERY_STUDENTS = {
    'url': 'http://grdms.bit.edu.cn/yjs/yanyuan/py/pyjxjh.do',
    'params': {
        'method': 'viewMingDan',
        'id': None
    }
}

GET_COURSES = {
    'url': 'http://grdms.bit.edu.cn/yjs/yanyuan/py/pyjxjh.do?method=stdSelectCourseEntry',
    'params': {
        'method': 'stdSelectCourseEntry'
    }
}

SELECT_COURSE = {
    'url': 'http://grdms.bit.edu.cn/yjs/dwr/call/plaincall/YYPYCommonDWRController.pyJxjhSelectCourse.dwr',
    'data': {
        'callCount': "1",
        'page': '/yjs/yanyuan/py/pyjxjh.do?method=stdSelectCourseEntry',
        'c0-scriptName': 'YYPYCommonDWRController',
        'c0-methodName': 'pyJxjhSelectCourse',
        'c0-id': '0',
        'c0-e1': 'string:2220170618',
        'c0-e2': 'string:1',
        'c0-e3': 'string:YY000000000000000000000000484779',
        'c0-e4': 'string:YY000000000000000000000000484779',
        'c0-e5': 'string:%E7%A1%95%E5%A3%AB',
        'c0-e6': 'string:%E7%BB%9F%E6%8B%9B%E7%BB%9F%E5%88%86%E7%A0%94%E7%A9%B6%E7%94%9F',
        'c0-e7': 'string:2017',
        'c0-e8': 'string:%E6%97%A0',
        'c0-e9': 'string:',
        'c0-param0': 'Object_Object:{xh:reference:c0-e1, lb:reference:c0-e2, studentId:reference:c0-e3, id:reference:c0-e4, pycc:reference:c0-e5, xslb:reference:c0-e6, nj:reference:c0-e7, ldfs:reference:c0-e8, ptlx:reference:c0-e9}',
        'c0-e10': 'string:YY000000000000000000000000484779',
        'c0-e11': 'string:2220170618',
        'c0-e12': 'string:1',
        'c0-e13': 'string:2018',
        'c0-e14': 'string:%E7%AC%AC%E4%B8%80%E5%AD%A6%E6%9C%9F',
        'c0-e15': 'string:402848c064580bb0016458a0dc4c0230',
        'c0-e16': 'string:1700001',
        'c0-e17': 'string:%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90',
        'c0-e18': 'string:',
        'c0-e19': 'string:%E4%B8%93%E4%B8%9A%E5%BF%85%E4%BF%AE%E8%AF%BE',
        'c0-e20': 'string:%E4%B8%93%E4%B8%9A%E5%BF%85%E4%BF%AE%E8%AF%BE',
        'c0-e21': 'string:32',
        'c0-e22': 'string:2',
        'c0-e23': 'string:',
        'c0-param1': 'Object_Object:{studentId:reference:c0-e10, xh:reference:c0-e11, lb:reference:c0-e12, xn:reference:c0-e13, xq:reference:c0-e14, teachClassId:reference:c0-e15, kcdm:reference:c0-e16, kczwmc:reference:c0-e17, kcywmc:reference:c0-e18, kcxz:reference:c0-e19, kclb:reference:c0-e20, xs:reference:c0-e21, xf:reference:c0-e22, ksfs:reference:c0-e23}',
        'batchId': '3',
    }
}

