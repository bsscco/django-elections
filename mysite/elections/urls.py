from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls), #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
]
