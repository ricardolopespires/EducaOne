from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.template.loader import render_to_string
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from datetime import datetime, date
from teachers.models import Teacher
from accounts.models import User
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.db import models









class Categorie(models.Model):
    icon = models.CharField(max_length=200, blank = True, null = True)
    name = models.CharField(max_length=200 )
    subcategorie = models.ManyToManyField('courses.SubCategorie', related_name= 'categoria_subcategoria', blank = True)	
    courses = models.ManyToManyField('courses.Course', related_name= 'course_categoria', blank = True)
    popularity = models.IntegerField(default = 0, help_text = 'O popularidade')
    featured = models.BooleanField(default = True)
	

    	

    def __str__(self):
        return self.name





class SubCategorie(models.Model):
	categorie = models.ForeignKey(Categorie, related_name = 'categoria', on_delete = models.CASCADE)
	icon = models.CharField(max_length=200, blank = True, null = True)
	name = models.CharField(max_length=200)
	subject = models.ManyToManyField('courses.Subject', related_name= 'subject_categoria', blank = True)	
	courses = models.ManyToManyField('courses.Course', related_name= 'course_subcategoria', blank = True)
	popularity = models.IntegerField(default = 0, help_text = 'O popularidade')
	

	def __str__(self):
		return self.name        



class Subject(models.Model):	
	icon = models.CharField(max_length=200, blank = True, null = True)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, )
	subcategorie = models.ManyToManyField('courses.SubCategorie', related_name= 'subject_subcategorie', blank = True)
	course = models.ManyToManyField('courses.Course', related_name= 'course_subject', blank = True)
	popularity = models.IntegerField(default = 0, help_text = 'O popularidade')	



	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title


class Level(models.Model):

	title = models.CharField(max_length=200)
	course = models.ManyToManyField('courses.Course', related_name= 'course_level', blank = True)


	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title




class Author(models.Model):
    profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(max_length=100, null=True)
    about = models.TextField()
    courses = models.ManyToManyField('courses.Course', related_name = 'author_course')

    def __str__(self):
        return self.name




class Course(models.Model):


	STATUS_CHOICES = (

		('projeto','projeto'),
        ('analizando','analizando'),
        ('aprovado','aprovado'),
        ('cancelado','cancelado')

        )

	STATUS_TYPE = (

		('mais vendido','Mais Vendido'),
        ('classificação mais alta','Classificação Mais Alta'),
        ('normal','Normal'),       

        )

	STATUS_SKILL = (

		('iniciantes', 'Iniciantes'),
		('intermediário','Intermediário'),
		('avançado','Avançado'),

		)


	owner = models.ForeignKey(User, related_name = 'author_course', on_delete = models.CASCADE)
	subject = models.ManyToManyField(Subject, related_name = 'assunto')
	categorie = models.ForeignKey(Categorie, related_name = 'Categoria', on_delete = models.CASCADE)
	info = models.CharField(max_length = 140, help_text = 'Resumo informativo do curso') 
	title = models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 200, unique = True)
	overview = RichTextField()	
	created = models.DateTimeField(auto_now_add = True)    
	updated = models.DateTimeField(auto_now = True,  blank = True)
	publish = models.DateTimeField(auto_now_add = False,  blank = True)
	status = models.CharField(max_length = 14, choices = STATUS_CHOICES, default = 'projeto')
	tipo = models.CharField(max_length = 40, choices = STATUS_TYPE, default = 'normal')
	level =  models.ForeignKey(Level, related_name ='Level_course', on_delete = models.CASCADE)
	popularity = models.IntegerField(default = 0, help_text = 'O popularidade')
	poster = models.URLField(blank = True)
	students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_joined',blank=True)	
	linguagem = models.CharField(max_length = 150, blank = True, null = True)    
	average_Rating = models.CharField(max_length =  3, blank = True , null = True, default = 0 )	
	likes = models.IntegerField(blank = True, null = True, default = 0)
	total_horas = models.CharField(max_length=150, default = '00:00:00')
	views = models.IntegerField(help_text = 'O total de visualizações', null = True, default = 0)	
	price = models.DecimalField(decimal_places = 2, max_digits = 10, default= 0, help_text = 'O preço do course')	
	discount = models.DecimalField(decimal_places = 2, max_digits = 10,  default= 0, help_text = 'Desconto no course')
	certificate = models.BooleanField(default = False, help_text = 'O curso tem Certificado')
	duration = models.DurationField( null=True,  default=timedelta(seconds=0))
	suggestion = models.BooleanField(default = False, help_text = 'Nossa principal sugestão para estudante')
	complete_per = models.IntegerField( validators = [MinValueValidator(0), MaxValueValidator(100)], default=0)


	

	class Meta:
		ordering = ['-created']


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'curso'
		verbose_name_plural = 'cursos'
		


class Module(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	course = models.ForeignKey(Course, related_name='modules',  on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	order = models.IntegerField(help_text = 'O numero de classificação do modulo', null = True, default = 0)
	description = models.TextField(blank=True)
	duration= models.DurationField( null=True,  default=timedelta(seconds=0))
	content = models.ManyToManyField('courses.Lesson', related_name = 'module_lesson', help_text= "conteúdo dos aulas") 
	is_active = models.BooleanField()
	


	class Meta:
		ordering = ['order']

	def __str__(self):
		return '{}. {}'.format(self.order, self.title)



class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default = 0)
    file = models.FileField(upload_to='videos',validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    duration = models.DurationField( null=True,  default=timedelta(seconds=0))
    preview = models.BooleanField(default = False)
    is_active  = models.BooleanField( default = False)
    concluded = models.BooleanField( default = False)


    class Meta:
    	ordering = ['order']

    def __str__(self):
    	return '{}. {}'.format(self.order, self.title)




class Learn(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	course = models.ForeignKey(Course, related_name = 'learn_course', on_delete = models.CASCADE)
	title = models.CharField(max_length = 40, help_text = 'O que você vai aprender')

	def __str__(self):
		return f'{self.title}'



class Requirement(models.Model):

	id = models.CharField(max_length = 150, primary_key = True)
	course = models.ForeignKey(Course, related_name = 'requirements_course', on_delete  = models.CASCADE)
	title = models.CharField(max_length = 40, help_text = 'O que você vai aprender')

	def __str__(self):
		return f'{self.title}'



class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'user_course_review', on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length = 290, help_text = 'Titulo da avaliação')
	message = models.TextField(help_text = 'O conteúdo da messagem')
	date = models.DateTimeField(auto_now_add=True)		
	rate = models.FloatField()
	
	
	def __str__(self):
		return self.user.username


	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Reviews'



class Visualizacao(models.Model):
	student = models.ForeignKey(User, related_name = 'student_views', on_delete = models.CASCADE)
	course = models.ForeignKey(Course, related_name = 'course_view', on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now_add = False)
	created = models.DateTimeField(auto_now_add = True)    
	updated = models.DateTimeField(auto_now = True,  blank = True)
	ultimo = models.IntegerField(default = 0)
	total = models.IntegerField()

	def __str__(self):
		return f'{self.student}'


	class Meta:
		verbose_name = 'Visualização'
		verbose_name_plural = 'Visualizações'


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, related_name='user_course_like')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.course



    class Meta:
    	verbose_name = 'Like'
    	verbose_name_plural = 'Likes'





class Favorito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='user_favoritos')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='favoritos')
    adicionado = models.DateTimeField(auto_now_add = True, blank=True, null=True)


    def __str__(self):
        return f'{self.course}'


    class Meta:
    	verbose_name = 'Favorito'
    	verbose_name_plural = 'Favoritos'



class Promotion(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	course = models.ForeignKey(Course, related_name = 'Promotion_course', on_delete  = models.CASCADE)
	inicio = models.DateTimeField(auto_now_add = False)    
	termino = models.DateTimeField(auto_now = False,  blank = True)
	is_active = models.BooleanField(default = False, help_text = 'A promoção está ativa')


	def __str__(self):
		return f'{self.course}'

	class Meta:
		verbose_name = 'Promoção'
		verbose_name_plural = 'Promoções'




class Share(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	course = models.ForeignKey(Course, related_name = 'Share_course', on_delete  = models.CASCADE)
	name = models.CharField(max_length = 70, help_text = 'O nome da pessoa que vai receber o dados do curso')
	email = models.EmailField('E-mail', help_text = 'O email que vai receber a promo do curso')
	inicio = models.DateTimeField(auto_now_add = False)    
	termino = models.DateTimeField(auto_now = False,  blank = True)
	is_active = models.BooleanField(default = False, help_text = 'A ativo para do email')

	def __str__(self):
		return f'{self.course}'

	class Meta:
		verbose_name = 'Promoção'
		verbose_name_plural = 'Promoções'


class Analytics(models.Model):

	
	owner = models.ForeignKey(User, related_name = 'author_course_analytics', on_delete = models.CASCADE)
	course = models.ForeignKey(Course, related_name = 'analytics_course', on_delete  = models.CASCADE)
	created = models.DateTimeField(auto_now_add = True)    
	updated = models.DateTimeField(auto_now = True,  blank = True)
	module = models.IntegerField(default = 0, help_text = "A quantidade modulos", blank = True, null = True)
	lesson = models.IntegerField(default = 0, help_text = "A quantidade lesson", blank = True, null = True)
	views = models.IntegerField(default = 0, help_text = "A quantidade lesson", blank = True, null = True)
	duration = models.DurationField( default = 0, blank = True, null = True)
	time = models.DurationField( default = 0, blank = True, null = True)
	rating = models.FloatField(default = 0 , help_text = 'A média de pontuação', blank = True, null = True)
	students = models.IntegerField(default = 0, help_text = "A quantidade alunos", blank = True, null = True)
	complete_per = models.IntegerField(default = 0, help_text = "A quantidade lesson", blank = True, null = True)

	def __str__(self):
		return f'{self.course}'

	class Meta:
		verbose_name = 'Analytics'
		verbose_name_plural = 'Analyzes'



	def save(self, *args, **kwargs):
		if self.lesson == 0 and self.views == 0:
			self.complete_per = 0
		else:
			self.complete_per = (self.views /self.lesson)* 100
			
		super().save(*args, **kwargs)

