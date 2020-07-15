import pytest

from tools.data import excel_tool
from tools.api import request_tool

'''
自动生成 数字 20，80 
自动生成 字符串 2 中文数字字母特殊字符 fuyan
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''



def test_signup(pub_data):
    pub_data["username"] = "自动生成 字符串 2 数字 fuyan"
    pub_data["phone"] = "自动生成 手机号"
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    url = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "phone": "${phone}",
  "pwd": "aAMjeZN9",
  "rePwd": "aAMjeZN9",
  "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"cstId": '$.data.cstId'}]
    request_tool.request(json_path=json_path, method=method, url=url, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)


def test_login(pub_data):
    pub_data["username"] = "自动生成 字符串 2 数字 fuyan"

    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
        "pwd": "aAMjeZN9",
        "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"cstId": '$.data.cstId'}]
    request_tool.request(json_path=json_path, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)


def test_cst_realname(pub_data):
    pub_data["certno"] = "自动生成 身份证号"
    pub_data["cstName"] = "自动生成 姓名"
    pub_data["email"] = "自动生成 邮箱"
    headers = {"token": pub_data["token"]}
    method = "POST"
    feature = "用户模块"
    story = '用户实名认证'
    title = "全字段正常流_1"
    uri = "/cst/realname2"
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "cstId": 2,
  "customerInfo": {
    "birthday": "2000-01-01",
    "certno": "${certno}",
    "city": "上海",
    "cstName": "${cstName}",
    "email": "${email}",
    "province": "上海",
    "sex": 1
  }
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"cstId": '$.data.cstId'}]
    request_tool.request(json_path=json_path, headers=headers, method=method, url=uri, pub_data=pub_data,
                         json_data=json_data, status_code=status_code, expect=expect, feature=feature, story=story,
                         title=title)



def test_post_json(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "aAMjeZN9",
  "userName": "fuyan86"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"cstId": '$.data.cstId'}]
    request_tool.request(json_path=json_path, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)


data = excel_tool.get_test_case("D:\\softwareData\\workspace\\auto_api\\test_case\\users\\充值测试.xls")


@pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])

def test_getAccInfo(pub_data,account_name,money,expect):
    pub_data["account_name"]=account_name
    pub_data["money"]=money
    pub_data["expect"] = expect
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": "${money}"}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
               'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    params = {'accountName': 'fuyan86'}
    status_code = 200  # 响应状态码
    expect = "2000" # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                         expect=expect, feature=feature, story=story, title=title, params=params)


def test_withdraw(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
               'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084',
               'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    json_data = '''{
   "accountName": "fuyan86",
   "cardNo": "6244548187141",
   "changeMoney":330
}'''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                         expect=expect, feature=feature, story=story, title=title, json_data=json_data)


def test_accLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '账户冻结'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    headers = {'Host': 'http://192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://qa.yansl.com:8084',
               'Referer': 'http://qa.yansl.com:8084/swagger-ui.html?urls.primaryName=user%20apis',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    data = {'accountName': 'fuyan86'}

    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                         expect=expect, feature=feature, story=story, title=title, data=data)


def test_accUnLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '账户解冻'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://192.168.1.151:8084',
               'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    data = {'accountName': 'fuyan86'}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                         expect=expect, feature=feature, story=story, title=title, data=data)
