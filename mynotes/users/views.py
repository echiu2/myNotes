from django.shortcuts import render, HttpResponse, redirect
from .forms import signupForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = signupForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)
