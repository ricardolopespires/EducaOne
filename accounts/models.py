from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from ckeditor.fields import RichTextField
from phone_field import PhoneField
from django.core import validators
from django.utils import timezone
from django.conf import settings
from django.db import models
import re



class User(AbstractBaseUser, PermissionsMixin):


    STATUS_CHOICES = (
                        ('ativos','Ativos'),
                        ('pendentes','Pendentes'),
                        ('inativos','Inativos'),
                     )

    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True, 
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    address = models.CharField('Endereço', max_length = 190, blank = True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    expert = models.ManyToManyField('courses.SubCategorie', related_name = 'expert_course')
    description = RichTextField( blank = True, null = True)
    state = models.CharField('Estado',  max_length = 100, blank = True)
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = 'projeto')
    city = models.CharField('Cidade', max_length = 190, blank = True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)    
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    img = models.ImageField(upload_to = 'user')
    teachers = models.ManyToManyField('courses.Course', related_name = 'teachers_course', blank = True)
    students = models.ManyToManyField('courses.Course', related_name = 'student_course', blank = True)
  
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    
 


class Newsletter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='usuário_newsletter',
       related_name='usuário_newsletter', on_delete = models.CASCADE, blank = True, null = True )
    email = models.EmailField()

    def __str__(self):
        return self.email



class Experiencia(models.Model):
    nivel = models.IntegerField(default = 0)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'experiências', blank=True)    
    percent = models.IntegerField(help_text = 'Porcetagem da Experiência', default = 0)
    pontuacao = models.IntegerField(help_text = 'Pontuação da Experiência', default = 0)
    total = models.IntegerField(help_text = 'total da Experiência do nivel', default = 0)
    is_active = models.BooleanField( default = False)



    def save(self, *args, **kwargs):

        porcentagem = 100
        try:
            calculo = porcentagem / self.total
        except ZeroDivisionError:
            calculo = porcentagem / 1
        self.percent = int(self.pontuacao * calculo)             

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'


    def __str__(self):
        return f'{self.nivel}, {self.porcentagem}'  



class habilidades(models.Model):    
    titulo = models.CharField(max_length = 450,)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'habilidades', blank=True)
    img = models.ImageField(upload_to = 'habilidades')
    pontuacao = models.IntegerField(default = 0)
    total = models.IntegerField(default= 1000) 
    percent = models.IntegerField(help_text = 'Porcetagem da habilidades', default = 0)


    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'



    def save(self, *args, **kwargs):

        porcentagem = 100

        try:
            calculo = porcentagem / self.total
        except ZeroDivisionError:
            calculo = porcentagem / 1
        self.percent = int(self.pontuacao * calculo)

        super().save(*args, ** kwargs)
        

    def __str__(self):
        return f'{self.titulo}, {self.porcetagem}'   