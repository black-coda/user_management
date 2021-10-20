from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from .views import signup_view, new_sign_up_view

urlpatterns = [
    path('register/', new_sign_up_view, name='signup'),
    path("accounts/", include('django.contrib.auth.urls')),
    #path('captcha/',) #solo continue here
]