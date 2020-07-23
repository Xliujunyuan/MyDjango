from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('(?P<year>[0-9]{1,}).html',views.myyear,{'month':12},name='myyear'),
    path('download.html',views.download),
    path('show.html',views.index),
    path('login.html',views.login),
    path('index/',views.ProductList.as_view()),
    path('test.html',views.test)
]