from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import UserInfo


# 表单
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'name' in request.GET and 'password' in request.GET:
        # 使用 filter 查询
        users = UserInfo.objects.filter(name=request.GET['name'].strip())
        if users.exists():  # 检查是否有匹配的用户
            user = users.first()  # 获取第一条记录
            if user.password == request.GET['password'].strip():
                message = '你输入的用户名: ' + request.GET['name']
                pass_msg = '你输入的密码: ' + request.GET['password']
                return HttpResponse(message + '<br>' + pass_msg)
            else:
                return HttpResponse('用户名或者密码输入错误')
        else:
            return HttpResponse('用户名不存在')
    else:
        return HttpResponse('请输入用户名和密码')