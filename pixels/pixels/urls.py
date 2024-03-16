"""
URL configuration for pixels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# pixels/urls.py
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from services import views as service_views
urlpatterns = [
    path('', home_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
     path('login/', home_views.login_view, name='login'),
     path('signup/', home_views.signup_view, name='signup'),
     path('logout/', home_views.logout_view, name='logout'),
     path('service/<str:service>/', service_views.service_views, name='service'),
     path('dashboard/', home_views.dashboard, name='dashboard'),
    path('diabetes_prediction/', service_views.diabetes_prediction, name='diabetes_prediction'),
    path('dietcheck_result/', service_views.dietcheck_result, name='dietcheck_result'),
    path('heart_disease_prediction/', service_views.heart_disease_prediction, name='heart_disease_prediction'),
    path('handlesleep', service_views.handlesleep, name='handlesleep'),
    path('dummy/', home_views.dummy_view, name='dummy')
    # Add more URL patterns as needed
]

