import os
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from . import views

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Frontend')


def serve_file(filename, content_type='text/html'):
    def view(request):
        filepath = os.path.join(FRONTEND_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return HttpResponse(content, content_type=content_type)
        return HttpResponse('Not found', status=404)
    return view


def serve_image(request, filename):
    if filename.startswith('http://') or filename.startswith('https://'):
        return HttpResponseRedirect(filename)
    filepath = os.path.join(FRONTEND_DIR, 'images', filename)
    if os.path.exists(filepath):
        ext = os.path.splitext(filepath)[1].lower()
        content_types = {
            '.svg': 'image/svg+xml',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp',
        }
        content_type = content_types.get(ext, 'application/octet-stream')
        mode = 'r' if ext == '.svg' else 'rb'
        encoding = 'utf-8' if ext == '.svg' else None
        with open(filepath, mode, encoding=encoding) as f:
            content = f.read()
        return HttpResponse(content, content_type=content_type)
    return HttpResponse('Not found', status=404)


urlpatterns = [
    # API endpoints
    path('api/customers/add/', views.add_customer),
    path('api/customers/', views.get_customers),
    path('api/customers/update/<int:id>/', views.update_customer),
    path('api/customers/delete/<int:id>/', views.delete_customer),

    path('api/restaurants/add/', views.add_restaurant),
    path('api/restaurants/', views.get_restaurants),
    path('api/restaurants/update/<int:id>/', views.update_restaurant),
    path('api/restaurants/delete/<int:id>/', views.delete_restaurant),

    path('api/foods/add/', views.add_food),
    path('api/foods/', views.get_foods),
    path('api/foods/update/<int:id>/', views.update_food),
    path('api/foods/delete/<int:id>/', views.delete_food),

    path('api/cart/add/', views.add_cart),
    path('api/cart/', views.get_cart),
    path('api/cart/update/<int:id>/', views.update_cart),
    path('api/cart/delete/<int:id>/', views.delete_cart),

    path('api/orders/add/', views.add_order),
    path('api/orders/', views.get_orders),
    path('api/orders/update/<int:id>/', views.update_order),
    path('api/orders/delete/<int:id>/', views.delete_order),

    # Frontend pages
    path('', serve_file('index.html'), name='home'),
    path('index.html', serve_file('index.html'), name='home_html'),
    path('login.html', serve_file('login.html'), name='login'),
    path('register.html', serve_file('register.html'), name='register'),
    path('restaurants.html', serve_file('restaurants.html'), name='restaurants'),
    path('menu.html', serve_file('menu.html'), name='menu'),
    path('cart.html', serve_file('cart.html'), name='cart'),
    path('orders.html', serve_file('orders.html'), name='orders'),
    path('dashboard.html', serve_file('dashboard.html'), name='dashboard'),
    path('style.css', serve_file('style.css', 'text/css'), name='css'),
    path('script.js', serve_file('script.js', 'application/javascript'), name='js'),
    path('images/<path:filename>', serve_image),
]
