from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
# Create your views here.

def dashboard(request):
    return render(request,"user/home.html")


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('dashboard')

    else:
        SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})


def new_sign_up_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('firstname')
        user.profile.last_name = form.cleaned_data.get('lastname')
        user.profile.email = form.cleaned_data.get('email')

        # user cant login until link confirmed

        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        subject = 'Please activate your account'

        #load a template like *get_template*

        message = render_to_string('registration/activation_request.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            }
        )
        
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('dashboard')
    else:
        SignUpForm()

    return render(request, 'registration/register.html', {'form':form})
    
