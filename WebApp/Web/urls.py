from django.conf.urls import url, include
from . import views

app_name = 'Web'

urlpatterns =[
    url(r'^$', views.home),
    url(r'^login/$', views.login, name='login'),
    url(r'^SignUp/$', views.SignUp, name='SignUp'),
    url(r'^error_404/$',views.error_404,name='Error 404'),
    url(r'^error_500/$',views.error_500,name='Error 500'),

]

