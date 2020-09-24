from django.contrib import admin
from django.contrib.auth.models import User
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
#admin.site.register(User)