from django.urls import path
from . import views

app_name='registro'
urlpatterns = [
	#ex /
	path('',views.IndexView.as_view(), name='index'),
	#ex /
	path('formato/',views.FormatoView.as_view(), name='formato'),
	#ex /
	path('registro/',views.registro, name='registro'),
	#ex
	path('completo/',views.SuccessView.as_view(), name='completo'),
]