from .models import Contact, Newsletter
from django import forms






class Contact_Form(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name','email','dias','message']



class Newsletter_Form(forms.ModelForm):

	class Meta:
		model = Newsletter
		fields = ['name','email']
