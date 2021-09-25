from django.urls import include, path
from login import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
]