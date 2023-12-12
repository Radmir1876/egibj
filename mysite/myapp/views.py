from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    context = {
        'full_name': 'Your Name',
        'height': 'Your Height',
        'weight': 'Your Weight',
        'age': 'Your Age',
    }
    return render(request, 'myapp/about.html', context)

def contacts(request):
    context = {
        'contacts': {
            'Phone': 'Your Phone',
            'Social': 'Your Social',
            # Add more contacts here
        },
    }
    return render(request, 'myapp/contacts.html', context)

def form(request):
    return render(request, 'myapp/form.html')

from .forms import RegistrationForm

def form(request):
    form = RegistrationForm()
    return render(request, 'myapp/form.html', {'form': form})