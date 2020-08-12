"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include 
from django.contrib.auth import views as auth_views 
from django.contrib.auth.decorators import login_required
from user import views as user_views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('gram.urls')),
    url(r'^register/', user_views.register, name='register'),
    url('profile/', user_views.profile, name='profile'),
    url(r'^editprofile/', user_views.edit_profile, name='edit_profile'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)