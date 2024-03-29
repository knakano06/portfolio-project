"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# importing the settings file we have in portfolio file
from django.conf import settings
# static allows us to serve image files and other files as well
from django.conf.urls.static import static

# import the views.py file in jobs and blog app
import jobs.views
import blog.views

urlpatterns = [
    # path to admin site
    path('admin/', admin.site.urls),

    # go to jobs apps, views.py, and go to the home function
    path('', jobs.views.home, name = 'home'),

    # 'blog/' can be any name but 'blog.urls' has to refer to the name of the app
    # this will forward you to url.py in the blogs app
    path('blogs/', include('blog.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# above code will refer to settings.py
