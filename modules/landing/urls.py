from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name="index"),
    #url(r'^singup/$',singup, name="singup"),
    url(r'^login/$', login, name="login"),
    url(r'^signup/$', signup,name="signup"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^matchs/$', matchs, name="matchs"),
    url(r'^new/image/$', uploadImage, name="uploadImage")
]