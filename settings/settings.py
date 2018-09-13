LOGIN = {
    'url': 'https://login.bit.edu.cn/cas/login',
    'params': {
        'service': 'http://grdms.bit.edu.cn/yjs/login_cas.jsp'
    },
}

QUERY_CLASS = {
    'url': 'http://grdms.bit.edu.cn/yjs/yanyuan/py/pyjxjhQuery.do',
    'params': {
        'method': 'query',
        'index': 'end',
        'pager.offset': "0",
    },
    'data': {
        "criteria": "kkxn = '%s' and kkxq = '%s'",
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

GET_ENGINE_JS = {
    'url': 'http://grdms.bit.edu.cn/yjs/dwr/engine.js'
}

SELECT_COURSE = {
    'url': 'http://grdms.bit.edu.cn/yjs/dwr/call/plaincall/YYPYCommonDWRController.pyJxjhSelectCourse.dwr',
    'data': {
        'callCount': "1",
        'page': '/yjs/yanyuan/py/pyjxjh.do?method=stdSelectCourseEntry',
        'httpSessionId': None,
        'scriptSessionId': None,
        'c0-scriptName': 'YYPYCommonDWRController',
        'c0-methodName': 'pyJxjhSelectCourse',
        'c0-id': '0',
        'c0-param0': 'Object_Object:{xh:reference:c0-e1, lb:reference:c0-e2, studentId:reference:c0-e3, id:reference:c0-e4, pycc:reference:c0-e5, xslb:reference:c0-e6, nj:reference:c0-e7, ldfs:reference:c0-e8, ptlx:reference:c0-e9}',
        'c0-param1': 'Object_Object:{studentId:reference:c0-e10, xh:reference:c0-e11, lb:reference:c0-e12, xn:reference:c0-e13, xq:reference:c0-e14, teachClassId:reference:c0-e15, kcdm:reference:c0-e16, kczwmc:reference:c0-e17, kcywmc:reference:c0-e18, kcxz:reference:c0-e19, kclb:reference:c0-e20, xs:reference:c0-e21, xf:reference:c0-e22, ksfs:reference:c0-e23}',
        'batchId': '3',
    }
}
