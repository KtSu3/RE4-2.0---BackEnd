from django.contrib import admin
from django.urls import path, include
from App import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('App.urls')),
    path('apiP/', include('App.urls')),

    
    
]   

