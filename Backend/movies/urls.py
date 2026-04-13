from django.urls import path
from .views import TestAuthView

urlpatterns = [
    path('test/', TestAuthView.as_view()),
]

from .views import RegisterView

urlpatterns = [
    path('test/', TestAuthView.as_view()),
    path('register/', RegisterView.as_view()),
]