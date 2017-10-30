from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^signin/$', views.LoginView.as_view(), name="login_view"),
    url(r'^signup/$', views.SignUp.as_view(), name='signup_view'),

]