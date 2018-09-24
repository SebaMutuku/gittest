"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import handler404,handler500,handler400,handler403
from django.conf.urls import static
from django.conf import settings
from Web import views as webviews


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Web/',include('Web.urls')),

] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404=webviews.error_404
handler500=webviews.error_500
handler403=webviews.error_403
handler400=webviews.error_400
