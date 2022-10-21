from django.contrib import admin
from .models import User, Skill, Education
# Register your models here.
admin.site.register(Education)
admin.site.register(User)
admin.site.register(Skill)


