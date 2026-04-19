#Alans
from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse

def test(request):
    return HttpResponse("CONFIG URLS WORKING")

urlpatterns = [
    # Yegors
    path('admin/', admin.site.urls),
    path('test/', test),
    
    # Yerdaulet & Alans
    path('api/', include('movies.urls')),
]