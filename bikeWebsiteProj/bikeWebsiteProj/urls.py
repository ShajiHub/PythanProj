"""bikeWebsiteProj URL Configuration

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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from bw import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('about',views.about, name = 'about'),
    path('contact',views.contact, name = 'contact'),
    path('shop',views.shop, name = 'shop'),
    path('gallery',views.gallery, name = 'gallery'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name = 'logout'),
    path('signup',views.signup, name = 'signup'),
    path('profile',views.profile, name = 'profile'),
    path('kidsbike',views.kidsbike, name = 'kidsbike'),
    path('womensbike',views.womensbike, name = 'womensbike'),
    path('mensbike',views.mensbike, name = 'mensbike'),
    path('sportsbike',views.sportsbike, name = 'sportsbike'),
    path('accessories',views.accessories, name = 'accessories'),
    path('cart',views.cart, name = 'cart'),
    path('sitedata',views.sitedata, name='sitedata'),
    path('logout',views.logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
