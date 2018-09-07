"""MSB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/user.0/topics/http/urls/
Examples:
Function views
    templates. Add an import:  from my_app import views
    user. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    templates. Add an import:  from other_app.views import Home
    user. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfg
    templates. Import the include() function: from django.urls import include, path
    user. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls')),
    path('comment/', include('comment.urls')),
    path('likes/', include('likes.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
