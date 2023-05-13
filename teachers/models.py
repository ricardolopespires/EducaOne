from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.




class Teacher(models.Model):


		
	name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name ='teacher_course', on_delete=models.CASCADE)
	picture = models.ImageField(upload_to = 'user', blank = True, null  = True)
	slug = models.SlugField(null = True, unique = False)
	expert = models.CharField(max_length = 190, help_text = 'A habilidade do instrutor', null  = True)
	description = RichTextField(blank = True, null = True)	
	courses = models.ManyToManyField('courses.Course', related_name = 'course_author', blank = True)	
	rating = models.FloatField(default = 0, help_text = 'Avaliação do instrutor')
	reviews = models.IntegerField(default = 0, help_text = 'Comentários dos alunos')
	students = models.ManyToManyField('accounts.User',related_name='students_enrolled', blank=True)
	is_active = models.BooleanField( default = False)	

	

	def __str__(self):
		return f'{self.name}'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural = 'Autores'





class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'user_instrutor_review', on_delete=models.CASCADE)
	course = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	title = models.CharField(max_length = 290, help_text = 'Titulo da avaliação')
	message = models.TextField(help_text = 'O conteúdo da messagem')
	date = models.DateTimeField(auto_now_add=True)	
	rate = models.FloatField()
	
	
	def __str__(self):
		return self.user.username


	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Reviews'