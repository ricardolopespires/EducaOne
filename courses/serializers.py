
from rest_framework import serializers 
from .models import Lesson, Analytics




class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = ['id','title','concluded']



class AnalyticsSerializers(serializers.ModelSerializer):

	class Meta:

		model = Analytics
		fields = ['id','course','views']