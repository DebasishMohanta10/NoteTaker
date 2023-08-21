from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.views import LoginView,LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib.auth import login
from django.views import View

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

class TaskLogoutView(LogoutView):
    pass


class SignupView(View):
    template_name = "auth/signup.html"
    
    def get(self,request):
        return render (request , self.template_name)
    
    def post(self,request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('notes')
        else:
            return render (request , self.template_name)