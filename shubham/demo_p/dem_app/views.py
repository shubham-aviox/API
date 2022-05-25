from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View
from .models import Student
# Create your views here.


def home(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Already taken")
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Already taken")
                return redirect('/')
            else:
                user=User.objects.create_user(first_name=fname, last_name=lname,username=username, email=email, password=password1)
                user.save()
                messages.success(request, "User has been created")
        else:
            messages.warning(request, "Password did not match")
    else:
        return render(request, 'index.html')
    return render(request, 'index.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in")
        else:
            messages.warning(request, "creadentials wrong")
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# register the student with class based View
class StudentView(View):
    def get(self, request):
        student = Student.objects.all()
        return render(request, 'student.html', {'students': student})
    
    def post(self, request):
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        if Student.objects.filter(roll_number=roll_number).exists():
            messages.success(request, 'This roll number already taken')
            return redirect('studentregister')
        else:
            student = Student(name=name, roll_number=roll_number, email=email, phone=phone, address=address)
            student.save()
            messages.success(request, 'Your information has saved')
            return redirect('studentregister')