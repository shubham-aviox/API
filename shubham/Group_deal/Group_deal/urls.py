"""Group_deal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from group_deal_app import views
from django.conf import settings  
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('sign', views.SignInView.as_view(), name='sign'),
    path('logout', views.logout_view, name='logout'),
    path('product_detail/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/<str:code>/', views.ResetPassword.as_view(), name='reset_password'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
