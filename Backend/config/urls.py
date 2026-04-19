# -------------------- Alans --------------------
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#Yegors
from django.contrib import admin
from django.http import HttpResponse

def test(request):
    return HttpResponse("CONFIG URLS WORKING")


# -------------------- COMBINED URLS --------------------
urlpatterns = [
    #Yegors
    path('test/', test),
    path('admin/', admin.site.urls),

    # ----Alans----
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),

    # ----Shared apps----
    path('api/', include('movies.urls')),
]