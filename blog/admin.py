from django.contrib import admin
from blog.models import Blog, Category, SlideShow, Gallery, Product_Type

class BlogAdmin(admin.ModelAdmin):
   # exclude = ['posted']
   prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}

class SlideShowAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}

class GalleryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}

class Product_TypeAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SlideShow, SlideShowAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Product_Type, Product_TypeAdmin)
