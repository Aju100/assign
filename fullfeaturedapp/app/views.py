from django.views import generic
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic import ListView,UpdateView,View
from .forms import LoginForm,SignupForm,UpdateForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import Post,Profile
from .forms import UpdateForm
from django.utils.decorators import method_decorator
User = get_user_model()

class ProfileView(View):
        def get(self,request,pk,*args,**kwargs):
                user = get_object_or_404(User,pk=pk)
                context ={
                        'user':user
                }
                return render(request,'app/profile.html',context)

class ProfileUpdateView(View):
        user = User()
        template_name='app/update_profile.html'

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
                return super().dispatch(*args, **kwargs)

        def get(self,request,pk,*args,**kwargs):
                update_form = UpdateForm
                context ={
                        'update_form':update_form
                }
                return render(request,self.template_name,context)

        def post(self,request,pk,*args,**kwargs):
                user = User.objects.get(pk=pk)
                update_form = UpdateForm(request.POST)
                print('data',request.POST)
                if update_form.is_valid():
                        user.first_name = update_form.cleaned_data['first_name']
                        user.last_name = update_form.cleaned_data['last_name']
                        user.password = update_form.cleaned_data['password']
                        user.save()
                        context= {
                                'pk':user.id
                        }
                        return redirect(reverse('profile'),context)
                        
                else:
                        context = {
                                'update_form':update_form
                        }
                        return render(request,self.template_name,context)
                


class BlogPostView(ListView):
        queryset = Post.objects.all()
        template_name = 'app/blog.html'

class LoginView(View):
        template_name = 'app/login.html'

        def get(self,request,*args,**kwargs):
                form = LoginForm()
                context = {
                        'form':form
                }
                return render(request,self.template_name,context)
        def post(self,request,*args,**kwargs):
                form = LoginForm(request.POST)
                if form.is_valid():
                        print(form.cleaned_data)
                        user =authenticate(
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password']
                        )
                        if user is not None:
                                login(request,user)
                                return redirect(reverse('home'))
                        else:
                                print('Form not valid')
                        return render(request,self.template_name,{'form':form})

class LogoutView(View):
        @staticmethod
        def get(request,*args,**kwargs):
                logout(request)
                return redirect(reverse('login'))

class SignupView(View):
        template_name = 'app/signup.html'

        def get(self,request,*args,**kwargs):
                form = SignupForm()
                print(form.as_p())
                return render(request,self.template_name,context={'form':form})

        def post(self,request,*args,**kwargs):
                form = SignupForm(request.POST)

                if form.is_valid():
                        user = User(
                                username=form.cleaned_data['username'],
                                first_name=form.cleaned_data['first_name'],
                                last_name=form.cleaned_data['last_name'],
                                email=form.cleaned_data['email'],
                        )
                        user.save()
                        user.set_password(form.cleaned_data['password1'])
                        user.save()
                        print('saved!')
                        return redirect(reverse('login'))
                else:
                        return render(request, self.template_name, context={'form':form})