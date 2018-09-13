from colorama import Fore
from automation.auto_login import AutoLogin
from automation.auto_watch import AutoWatcher
from automation.auto_select import AutoSelect

print(Fore.LIGHTBLUE_EX + "Author: CrazyK")
print(Fore.LIGHTBLUE_EX + "Time:   2018-09-12 21:20:22")

print(Fore.LIGHTBLUE_EX + "AutoSelectCourse 1.0.0 (Test)")
print(Fore.LIGHTBLUE_EX + "=" * 40)

print(Fore.LIGHTYELLOW_EX + "As a BITer, the most fuckable thing is taking courses when semester begin.")
print(Fore.LIGHTYELLOW_EX + "So I make a tool for the fuckable thing hoping to help you sincerely.\n")

print(Fore.RED + "Anything you do with the tool is none of my business, including fuck the jwc.")
print(Fore.LIGHTBLUE_EX + "=" * 40)

print(Fore.GREEN + "Welcome to AutoSelectCourse, make sure that you have completed settings.")

login = AutoLogin()
login.login()
watcher = AutoWatcher(login.session)
watcher.get_all_courses()
course_list = None

while True:
    print(Fore.LIGHTBLUE_EX + "=" * 40)
    print(Fore.GREEN + "Operations: ")
    print(Fore.GREEN + "1. Add courses.")
    print(Fore.GREEN + "2. Query students of course.")
    print(Fore.GREEN + "3. Start to fuck grdms.")
    print(Fore.GREEN + "4. Exit.")
    print(Fore.GREEN + "5. Help.")
    operation = input("Please choose operation: ")

    if operation == "1":
        course_list = watcher.crate_task_list()
    elif operation == "2":
        watcher.get_students_of_course()
    elif operation == "3":
        selector = AutoSelect(watcher.session, course_list)
        selector.run_and_wait()
    elif operation == "4":
        exit(0)
    elif operation == "5":
        print("""
        1. 添加课程，创建任务列表
        2. 查询选课的学生信息 -_-
        3. 开始抢课哦
        4. 退出
        5. 求求你了，告诉我咋用吧 `_`
        """)
    else:
        print("Enter again, wrong operation.")
        continue
