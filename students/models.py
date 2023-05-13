from courses.models import Course
from accounts.models import User
from django.conf import settings
from django.db import models

# Create your models here.









class Learning(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)	
	student = models.ForeignKey(User, related_name = 'student_learning', on_delete = models.CASCADE)
	course = models.ForeignKey(Course, related_name = 'course_learning', on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now_add = False)


	def __str__(self):
		return f'{self.student}'


	class Meta:
		verbose_name = 'Learning'
		verbose_name_plural = 'Learnings'