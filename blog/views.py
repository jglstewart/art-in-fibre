import math
from blog.models import Blog, Category, SlideShow, Gallery, Product_Type
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'most_recent_post': Blog.objects.all().order_by('-posted')[0],
        'second_recent_post': Blog.objects.all().order_by('-posted')[1],
        'first_slide': SlideShow.objects.all()[0],
        'second_slide': SlideShow.objects.all()[1],
        'third_slide': SlideShow.objects.all()[2]
    }, context_instance=RequestContext(request)
)

def view_post(request, slug):   
    return render_to_response('blog/blog_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    }, context_instance=RequestContext(request)
)

def view_by_category(request, slug, page):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/blog.html', {
        'posts': Blog.objects.filter(category = category)[((int(page)-1)*3):((int(page)*3))],
        'categories': Category.objects.all(),
        'pages': int(math.ceil( float(len(Blog.objects.filter(category=category)))/3.0)),
        'current_page': int(page)
}, context_instance=RequestContext(request)
)


def view_about(request):
    return render_to_response('blog/about.html', {
    }, context_instance=RequestContext(request)
)

def view_gallery(request, page):
    return render_to_response('blog/gallery.html', {
        'products': Gallery.objects.all()[((int(page)-1)*12):((int(page)*12))],
        'types': Product_Type.objects.all(),
        'pages': int(math.ceil( float(len(Gallery.objects.all()))/12.0)),
        'current_page': int(page)
    }, context_instance=RequestContext(request)
)

def view_product(request, slug):
    return render_to_response('blog/gallery_product.html', {
        'product': Gallery.objects.get(slug = slug)
    }, context_instance=RequestContext(request)
)

def view_blog(request, page):
    return render_to_response('blog/blog.html', {
    'posts': Blog.objects.all()[((int(page)-1)*3):((int(page)*3))],
    'catagories': Category.objects.all(),
    'pages': int(math.ceil( float(len(Blog.objects.all()))/3.0)),
    'current_page': int(page)
    }, context_instance=RequestContext(request)
)

def view_contact(request):
    return render_to_response('blog/contact.html', {
    },context_instance=RequestContext(request)
)
