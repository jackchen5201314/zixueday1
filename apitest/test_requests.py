import requests
import pytest
class Testrequests():
    @pytest.fixture()
    def test_token_get(self):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww0a755c411005b357&corpsecret=-tzXl87I-yRulX0ikZQGqnJ4Th2qfBgpRa_1H3FcmG0")
        print(r.json()['access_token'])
        return r.json()['access_token']

    def test_addmember_post(self):
        addmember_json={ "userid": "zhangs",
    "name": "张三",
    "alias": "jackzhan",
    "mobile": "+86 13800000066",
    "department": [1]}
        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_token_get()}",
                        json=addmember_json)
        print(r.json())
    def test_delemember_get(self):
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.test_token_get()}&userid=JiangXiaoMing")
        print(r.json())
    def test_updatemember_post(self):
        update_json={ "userid": "zhangs",
    "name": "张三哥",
    "alias": "jackzhan",
    "mobile": "+86 13800000066",
    "department": [1]}
        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_token_get()}",json=update_json)
        print(r.json())
    def test_search_get(self):
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.test_token_get()}&userid=JiangChen")
        print(r.json())
