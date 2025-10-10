# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# from django.contrib.auth.models import User  # User class (model)
# from .forms import RegisterForm  # registrer forms from forms.py


# # Create your views here.


# # AUTHENTICATION APP

# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             if username is not None and password is not None:
#                 user = User.objects.create_user(
#                     username=username, password=password)
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, "Username and password are required.")
#         else:
#             form = RegisterForm()
#             return render(request, 'accounts/register.html', {'form': form})


# def login_view(request):
#     error_message = None  # not sure what to do with this yet
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             next_url = request.POST.get(
#                 'next') or request.GET.get('next') or 'home'
#             return redirect(next_url)
#         else:
#             error_message = "Invalid Credentials!"
#     return render(request, 'accounts/login.html', {'error': error_message})


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login')
#     else:
#         return redirect('home')

# # home view
# # using the decorator


# @login_required
# def home_view(request):
#     return render(request, 'home/home.html')


# # protected view
# class ProtetedView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     # 'next' t redirect URL
#     redirect_field_name = 'rediret_to'

#     def get(self, request):
#         return render(request, 'registartion/protected.html')
