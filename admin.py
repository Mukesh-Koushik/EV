from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Products)
admin.site.register(Tasks)
admin.site.register(Prod_review)
admin.site.register(Idea_Forge)
admin.site.register(Orders)
admin.site.register(Sellers)
#admin.site.register(CustomUser)
admin.site.register(User_tasks)

