from django.shortcuts import render, render_to_response
from .forms import Signupform
from .models import User

def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.all()
            return render_to_response('user.html',{'user':user})

    else:
        form = Signupform()

    return render(request, 'singup.html', {'form':form})

# Returns list of registered users
def list_of_users(request):
    user = User.objects.all()
    return render(request, 'user.html',{'user':user})




