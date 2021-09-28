from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('register/', views.signup_view, name='signup'),
    path("accounts/", include('django.contrib.auth.urls')),
    #path('captcha/',) #solo continue here
]