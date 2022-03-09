from django.forms import ModelForm
from .models import *
class Newtodoform(ModelForm):
	class Meta:
		model = TodoIem
		fields = ['text']

