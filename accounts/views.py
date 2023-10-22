from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
User = get_user_model()

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token

from django.utils.encoding import force_str

# Create your views here.

def login_page(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
        
        else:
            messages.error(request, "Wrong credentials!")
            return redirect("login")

    context = {
        "form" : form
    }

    return render(request, "login.html", context)

def register_page(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.filter(email = email)
            if user:
                messages.info(request, "User with such an email already exits!")
                return redirect("register")
            else:    
                new_user = form.save(commit=False)
                new_user.is_active = False
                new_user.save()

                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account_activation_email.html', {
                    'user': new_user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                    'token': account_activation_token.make_token(new_user),
                })
                new_user.email_user(subject, message)

                return redirect("activation-required")
        else:
            messages.error(request, "Form is not valid!")
            return redirect("register")

    context = {
        "form":form
    }

    return render(request, "register.html", context)

@login_required
def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")

def activation_required(request):
    return render(request, "activation-required.html")

def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
    
    

    