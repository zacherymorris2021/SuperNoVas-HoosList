# accounts/views.py
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
# from .forms import UserRegisterForm


# class SignUp(generic.CreateView):
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

from django.shortcuts import render


def index(request):
    return render(request, 'signup.html')

def logout(request):
    return render(request, 'logout.html')
