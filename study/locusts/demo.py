# 保存为demo.py
# coding:utf-8
# from locust import HttpUser,TaskSet,task
#
# class BlogDemo(TaskSet):
#     '''用户行为：打开我的博客首页demo'''
#     @task(1)
#     def open_blog(self):
#         # 定义requests的请求头
#         r = self.client.get("/")
#         print(r.status_code)
#         assert r.status_code == 200
#
# class websitUser(HttpUser):
#     tasks = [BlogDemo]
#     min_wait = 3000  # 单位毫秒
#     max_wait = 6000  # 单位毫秒
#
# if __name__ == "__main__":
#     import os
#     os.system("locust -f demo.py --host=http://127.0.0.1:5000")
from locust import HttpUser, TaskSet, task


# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_index(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    task_create = UserBehavior
    min_wait = 3000
    max_wait = 6000
