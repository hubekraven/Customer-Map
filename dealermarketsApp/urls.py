from django.conf.urls import url

from . import views

app_name = 'dealermarketsApp'
#rlpatterns = [
#   url(r'^$', views.index, name='index'),
#	#url(r'^(?P<dealer_id>[0-9]+)/result/$', views.result, name='result'),
#	url(r'^result/$, result, {'template_name' : 'dealermarkets/result.html'}),


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/result/$', views.ResultsView.as_view(), name='result'),
]