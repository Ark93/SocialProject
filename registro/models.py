from django.db import models

# Create your models here.

class Miembro(models.Model):
	NumReg = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=100)
	ApellidoP = models.CharField(max_length=100)
	ApellidoM = models.CharField(max_length=100)
	CorreoE = models.CharField(max_length=200)
	FechaReg = models.DateField()
	Campo1 = models.CharField(max_length=200, default="")
	Campo2 = models.CharField(max_length=200, default="")
	Activo = models.BooleanField(default=True)
	def __str__(self):
		return ("Registro: %s %s %s %s " % (self.NumReg,self.Nombre,self.ApellidoP,self.ApellidoM))
	class Meta:
		unique_together = ["CorreoE"]