import qm_utils
import os

url = input("请输入登录URL: ")
cookie = qm_utils.qm_tools.get_cookie_from_url(url)
courses = qm_utils.qm_tools.get_courses(cookie)
print("课程列表（\033[32m绿色\033[0m为存在题库，\033[31m红色\033[0m为不存在题库）:")
for k, v in courses.items():
    is_found = "\033[31m" if not os.path.exists("qmyz/{}.csv".format(k)) else "\033[32m"
    print(f"{k:<5}{is_found}{v:<5}\033[0m")
course = input("请输入课程id: ")
num = int(input("请输入答题量(0为无限): "))
csv_list = os.listdir("qmyz")
if "{}.csv".format(course) not in csv_list:
    print("题库不存在")
    exit(1)
ti = qm_utils.qm.qm_tiku("qmyz/{}.csv".format(course))
qm = qm_utils.qm.qm_auto(url, ti.tiku, course, cookie)
qm.auto_do(num)
