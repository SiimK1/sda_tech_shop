from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account registered for {username}, you can now log in using your credentials.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')


class HomeView(ListView):
    template_name = 'home.html'
    model = Product
    context_object_name = 'products'

class CategoryView(ListView):
    template_name = 'categories.html'
    model = Product
    context_object_name = 'products'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ProductView(TemplateView):
    template_name = 'product.html'


