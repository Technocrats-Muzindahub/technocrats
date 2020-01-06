"""technocrats2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about-us/', views.aboutus, name="about"),
    path('contact/', views.contact, name="contact"),
    #path('bookings/', views.bookings, name='bookings'),
    #path('bookings/single-room', views.bookingsingle, name='bookingsingle'),
    #path('bookings/double-room', views.singleview, name='bookingsdouble'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/single-room', views.singleroom, name='singleroom'),
    path('rooms/double-room', views.doubleroom, name='doubleroom'),
    path('rooms/executive-room', views.executiveroom, name='executiveroom'),
    path('conference-room/', views.conferenceroom, name='conferenceroom'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

