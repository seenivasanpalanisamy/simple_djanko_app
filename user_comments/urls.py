from django.conf.urls import url
from user_comments import views

urlpatterns = [
	url(r'^create/$', views.create, name='create'),
	url(r'^update/$', views.update, name='update'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^details/$', views.details, name='details'),
	url(r'^about/$', views.about, name='about'),
	url(r'^home/$', views.stats, name='stats'),
	url(r'^', views.stats, name='default'),
]
"""NOT YET COMPLETED"""
handler404 = 'user_comments.views.handler404'
handler500 = 'user_comments.views.handler500'