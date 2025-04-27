from django.urls import path
from . import views, testdb, search, search2

urlpatterns = [
    path("", views.hello, name="hello"),
    path('runoob/', views.runoob, name="runoob"),
    path('testdb/', testdb.testdb, name="testdb"),
    path('search/', search.search, name="search"),
    path('search-form/', search.search_form, name="search_form"),
    path('search-post/', search2.search_post, name="search_post"),  # 确保路径正确
]
