from django.urls import path,include
from . import views, testdb, search, search2
from .views import add_emp

urlpatterns = [
    path('search/', search.search, name="search"),
    path('search-form/', search.search_form, name="search_form"),
    path('TestModel/', include('TestModel.urls')),
    path('register/', views.register, name="register")
]
