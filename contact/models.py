from django.utils import timezone
from django.db import models
from uuid import uuid4
# Create your models here.







class Contact(models.Model):

	id  =  models.UUIDField(primary_key = True, default = uuid4, editable = False)
	name = models.CharField(max_length = 150, help_text = "O nome da pessoas que mandando o mensagem")
	referente = models.DateTimeField(default = timezone.now, help_text = 'A data de referência' )
	dias = models.IntegerField(help_text = "quantidade de dia que estão em atraso", default = 0, blank = True, null = True)
	email = models.EmailField('E-mail', help_text = 'O email de resposta')
	message = models.TextField( help_text = "Conteudo da mensagem", blank = True)
	resposta = models.BooleanField(help_text = 'Se a messagem ja teve resposta', default = False)

	


	def __str__(self):
		return f'{self.name}'

	class Meta:

		verbose_name = 'messagem'
		verbose_name_plural = 'messagens'




class Newsletter(models.Model):
	
	id  =  models.UUIDField(primary_key = True, default = uuid4, editable = False)
	name = models.CharField(max_length = 150, help_text = "O nome da pessoas que mandando o mensagem", blank = True , null = True)
	referente = models.DateTimeField(default = timezone.now, help_text = 'A data de referência' )	
	email = models.EmailField('E-mail', help_text = 'O email de resposta')
	

	
	def __str__(self):
		return f'{self.name}'

	class Meta:

		verbose_name = 'Newsletter'
		verbose_name_plural = 'Newsletters'

