
# Register your models here.
from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ('id' , 'title' , 'body' , 'pub_date')
	list_display_links = ('id' , 'title')

	search_fields = ('id','title','body')
	list_per_page = 25


# Register your models here.
admin.site.register(Blog , BlogAdmin)
