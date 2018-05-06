from django.contrib import admin
from main.models import write_up , Author_detail , keywords , employer_work

# Register your models here.
admin.site.register(write_up)
admin.site.register(Author_detail)
admin.site.register(keywords)
admin.site.register(employer_work)