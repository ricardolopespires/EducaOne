from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
from django.db import models















class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):


	STATUS_CHOICES = (

		('projeto','projeto'),
        ('analizando','analizando'),
        ('aprovado','aprovado'),
        ('cancelado','cancelado')

        )

	id = models.CharField(max_length = 150, primary_key = True)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_created', on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	overview = models.TextField()
	created = models.DateTimeField(auto_now_add=True)    
	updated = models.DateTimeField(auto_now=True,  blank=True)
	publish = models.DateTimeField(auto_now_add =False,  blank=True)
	status = models.CharField(max_length = 14, choices = STATUS_CHOICES, default = 'projeto')
	popularity = models.IntegerField(default=0, help_text = 'O popularidade')
	poster = models.URLField(blank=True)
	poster_url = models.URLField(blank=True)
	#genero = models.ManyToManyField(Genre, blank=True)   
	#teachers = models.ManyToManyField(Author, blank = True,) 
	linguagem = models.CharField(max_length = 150, blank = True)    
	average_Rating = models.CharField(max_length =  3, blank = True )
	average_Count = models.CharField(max_length =  3, blank = True )
	votes_Count = models.IntegerField( default = 0)
	likes = models.IntegerField(blank = True, null = True, default = 0)
	total_horas = models.CharField(max_length=150, default = '00:00:00')
	views = models.IntegerField(default=0 , help_text = 'O total de visualizações')


	class Meta:
		ordering = ['-created']


	def __str__(self):
		return self.title

'''
class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
            ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)
'''

