from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('contacts', views.contactus, name='contacts'),
    path('pricing', TemplateView.as_view(template_name='pricing.html'), name='pricing'),
    path('products', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('add_cart', views.add_cart, name='add_cart'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('logout', views.logout, name='logout'),
    path('remove_cart', views.remove_cart, name='remove_cart'),
    path('feedback', views.feedback, name='feedback'),
]
