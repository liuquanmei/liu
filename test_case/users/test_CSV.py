import pytest

from tools.api import request_tool
from tools.data import excel_tool


data1 = excel_tool.get_test_case("D:\\softwareData\\workspace\\auto_api\\test_case\\users\\充值测试.xls")


@pytest.mark.parametrize("account_name,money,expect",data1[1],ids=data1[0])
def test_getaccinfo(pub_data,account_name,money,expect):
    pub_data["account_name"]=account_name
    pub_data["money"]=money
    pub_data["expect"] = expect
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers={"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": "${money}"}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
