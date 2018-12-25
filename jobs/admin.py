
# Register your models here.
from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
	list_display = ('id' , 'summary')
	list_display_links = ('id' , 'summary')

	search_fields = ('id',)
	list_per_page = 25


# Register your models here.
admin.site.register(Job , JobAdmin)
