from auto_tools import choose

session = choose.login()
courses = choose.get_courses(session)
choose.get_select_course_page(session)
choose.select_course(session)
