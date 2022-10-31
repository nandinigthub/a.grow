from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Contact

admin.site.register(Profile)
admin.site.register(Contact)