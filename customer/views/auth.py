

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView

from customer.models import User
from customer.views.token import account_activation_token
from customer.forms import LoginForm, RegisterModelForm
from django.views import View

'''class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customer')'''

class LoginPage(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm

    # success_url = reverse_lazy('customers')

    def get_success_url(self):
        return reverse_lazy('customers')
'''def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customer')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})'''

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

'''def logout_page(request):
    if request.method == 'GET   ':
        logout(request)
        return redirect('customers')
    return render(request, '')'''

'''class RegisterFormView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('customers')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.save()
        login(self.request, user)
        return redirect('customers')
class RegisterView(View):
    def get(self, request):
        form = RegisterModelForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('customers')'''


def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.is_active = False
            user.set_password(password)
            if not user.is_active:
                current_site = get_current_site(request)

                user = request.user
                subject = 'Verify Email'
                message = render_to_string('email/verify_email_message.html',{
                    'request': request,
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),

                })
                email = EmailMessage(subject, message, to=[user.email])
                email.send()
                return redirect('verify_email_done')

            send_mail('AnonyUser','you successfully registered !', settings.DEFAULT_FROM_EMAIL,[user.email], fail_silently=False)


    else:
        form = RegisterModelForm()

    return render(request, 'auth/register.html', {'form': form})

def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')
    else:
        messages.warning(request, 'The link is invalid.')

    return render(request, 'email/verify_email_confirm.html')

def verify_email_done(request):
    return render(request, 'email/verify_email_done.html')

def verify_email_complete(request):
    return render(request, 'email/verify_email_complete.html')