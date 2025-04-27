from django.http import HttpResponse

from TestModel.models import Test,BookInfo,UserInfo


# 数据库操作
def testdb(request):
    test2 = UserInfo.objects.create(name='hcg',password='123456',sex='True')
    test2.save()
    return HttpResponse("<p>数据添加成功！</p>")


