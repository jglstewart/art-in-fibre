from django.db import models
from django.db.models import permalink

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    main_image = models.ImageField(upload_to = 'main_images/', null = True, blank = True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    first_image = models.ImageField(upload_to = 'blog_images/', null = True, blank = True)
    second_image = models.ImageField(upload_to = 'blog_images/', null = True, blank = True)
    third_image = models.ImageField(upload_to = 'blog_images/', null = True, blank = True)
    fourth_image = models.ImageField(upload_to = 'blog_images/', null = True, blank = True)
    fifth_image = models.ImageField(upload_to = 'blog_images/', null = True, blank = True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class SlideShow(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'slideshow_images/', null = True, blank = True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_slideshow_entry', None, { 'slug': self.slug })

class Gallery(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    main_image = models.ImageField(upload_to = 'gallery_images/', null = True, blank = True)
    product_category = models.ForeignKey('blog.Product_Type')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_gallery_entry', None, { 'slug': self.slug })


class Product_Type(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_gallery_type', None, { 'slug': self.slug })
