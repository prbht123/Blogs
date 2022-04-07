from django.contrib import admin
from .models import Blog,Category,PostImages,Contact,Tag
# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(PostImages)
admin.site.register(Contact)
admin.site.register(Tag)