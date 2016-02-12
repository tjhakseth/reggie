from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/information/form/$', views.user_information_form, name='user_information_form'),
    url(r'^submit/user/information/form/$', views.submit_user_information_form, name='submit_user_information_form'),
]
