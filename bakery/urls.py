from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Static pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    
    # cart
      path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),


    # Categories & products
    path('categories/', views.category_list, name='category_list'),
    path('products/', views.product_list, name='product_list'),
    
    path('products/<str:category_name>/', views.category_view, name='category_view'),
    path('product/<str:product_slug>/', views.product_detail, name='product_detail'),

    # Delivery & payment (using IDs)
    path('delivery/<int:product_id>/', views.delivery_detail, name='delivery_detail'),
    path('payment/<int:product_id>/', views.payment_view, name='payment'),

    # Wishlist URLs
path('wishlist/', views.wishlist_view, name='wishlist'),
path('wishlist/add/<str:product_slug>/', views.add_to_wishlist, name='add_to_wishlist'),
path('wishlist/remove/<str:product_slug>/', views.remove_from_wishlist, name='remove_from_wishlist'),
path('wishlist/toggle/<str:product_slug>/', views.toggle_wishlist, name='toggle_wishlist'),


    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),

    
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

