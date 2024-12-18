from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include  # Make sure you include 'include'
from app13 import views  # Import views from the accounts app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', views.index, name='home'),  # Home route that renders the homepage (index.html)
    path('app13/', include('app13.urls')),  # Route for accounts-related views (signin/signup)
]



urlpatterns = [
    path('index/',views.index,name='index'),
    path('signin/', views.signin, name='signin'),  # URL for Sign In page
    path('signup/', views.signup, name='signup'),  # URL for Sign Up page
]