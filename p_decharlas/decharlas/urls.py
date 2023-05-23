from django.urls import path
from . import views

urlpatterns = [
	path('', views.general),
    path('config', views.config),
	path('help', views.help),
	path('login', views.login),
	path('logout', views.logout),
	path('<str:resource>', views.rsc),
	path('json/<str:resource>', views.jsonrsc),
	path('dyn/<str:resource>', views.dynrsc),
]