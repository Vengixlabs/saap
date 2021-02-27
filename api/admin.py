from django.contrib import admin

# Register your models here.
from .models import Posts

admin.site.register(Posts)
admin.site.site_header = 'Ronix by ash'