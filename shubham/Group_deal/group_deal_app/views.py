import email
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from .models import ForgetPassword, Product, RelatedImage
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
import uuid
from django.conf import settings 

User = get_user_model()


# Create your views here.
class HomeView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'index.html', {'products': product})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in success')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.warning(request, 'Please check your credentials')
            return redirect('login')


class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'sign-up.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        re_pass = request.POST['re_pass']
        phone = request.POST['phone']

        if name and password and email and phone:
            try:
                User.objects.get(email=email)
                messages.warning(request, 'This email has been taken')
                return redirect('sign')
            except User.DoesNotExist:
                user = User.objects.create_user(first_name=name, email=email, password=password, phone=phone, username=email)
                user.save()
                messages.success(request, 'You have registered successfully')
                return redirect('login')
        else:
            messages.warning(request, 'Please enter all required fields')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        relate_image = RelatedImage.objects.filter(product=product)
        return render(request, 'product-detail.html', {'products': product, 'relate_image': relate_image})


class ForgetPasswordView(View):
    def get(self, request):
        return render(request, 'forget.html')

    def post(self, request,*args, **kwargs):
        try:
            email = request.POST.get('email')
            id1 = User.objects.get(email=email)
            print(id1.id)
            User.objects.filter(email=email).exists()
            verification_code = uuid.uuid4()
            url = settings.BASE_URL + 'reset_password/' + str(verification_code)
            print(url)
            user = ForgetPassword(verification_code=verification_code, user_id=id1.id)
            user.save()
            print(verification_code)
            return render(request, 'check_email.html')
        except User.DoesNotExist:
            print("Invalid email")
            messages.info(request, 'email does not exist')
            return render(request, 'forget.html')

class ResetPassword(View):
    def get(self, request, *args, **kwargs):
        code = self.kwargs.get('code')
        return render(request, 'reset.html')

    def post(self, request,*args, **kwargs):
        code = self.kwargs.get('code')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            forget_password_obj = ForgetPassword.objects.get(verification_code=code)
            # print(forget_password_obj.user, 'uuuuuuuuuuu')
            if forget_password_obj.user in User.objects.all():
                user = User.objects.get(username=forget_password_obj.user)
                user.set_password(password)
                user.save()
                print('SSSSSSSSSSSSS')
            messages.info(request, 'your password has been changed')
            return redirect('/')
        else:
            messages.warning(request, 'Password did not match')
            return render(request, 'reset.html')


class SocialAccountLogin(View):
    def get(self, request):
        pass
        