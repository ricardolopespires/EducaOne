from ckeditor.fields import RichTextField
from courses.models import Categorie
from django.utils import timezone
from django.conf import settings
from django.db import models

# Create your models here.






class Post(models.Model):
  STATUS_CHOICES = (

  	('projeto', 'Projeto'),
  	('pedente','Pedente'),
  	('publicado', 'Publicado'),

  	)
  
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250, unique_for_date='publish')
  author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='blog_posts')
  categorie = models.ForeignKey(Categorie, related_name = 'blog_ctegorie', on_delete = models.CASCADE)
  overview = RichTextField()
  img = models.ImageField(upload_to = 'post', blank = True)
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')

  class Meta:
    ordering = ('-publish',)

  def __str__(self):
    return self.title
