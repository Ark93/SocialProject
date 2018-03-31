from django.shortcuts import render
from django.views import generic
from .models import Miembro
from datetime import date
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(generic.TemplateView):
	template_name="registro/index2.html"

class FormatoView(generic.TemplateView):
	template_name="registro/formaRegistro.html"

def registro(request):
	try:
		nombre_ = request.POST['nombre']
		apellidoP_ = request.POST['apellidoP']
		apellidoM_ = request.POST['apellidoM']
		correoE_ = request.POST['email']
		fecha_ = date.today()
		nota1_ = request.POST['nota1']
		nota2_ = request.POST['nota2']
		m = Miembro(Nombre=nombre_,ApellidoP=apellidoP_,ApellidoM=apellidoM_,CorreoE=correoE_,FechaReg=fecha_,Campo1=nota1_,Campo2=nota2_)
		#m.save()
	except Exception as e:
		print(e)
	return HttpResponseRedirect("/registro/completo")

class SuccessView(generic.TemplateView):
	template_name="registro/registroCompleto.html"