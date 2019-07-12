from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Estacionamiento
from .forms import EstacionamientoForm
from .forms import EstacionamientoeForm

def inicio(request):
    posts = Estacionamiento.objects.all()
    return render(request, 'home.html', {'posts': posts})
def publico(request):
    posts = Estacionamiento.objects.all()
    return render(request, 'home2.html', {'posts': posts})
def detest(request, pk):
    post = get_object_or_404(Estacionamiento, pk=pk)
    return render(request, 'detest.html', {'post': post})
def newest(request):
    if request.method == "POST":
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detest', pk=post.pk)
    else:
        form = EstacionamientoForm()
    return render(request, 'newest.html', {'form': form})

def arrendar(request, pk):
    post = get_object_or_404(Estacionamiento, pk=pk)
    if request.method == "POST":
        form = EstacionamientoeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if post.estado == 'NO DISPONIBLE':
                post.estado = 'DISPONIBLE'
            else:
                post.estado = 'NO DISPONIBLE'
            post.save()
            return redirect('detest', pk=post.pk)
    else:
        form = EstacionamientoeForm(instance=post)
    return render(request, 'arrendar.html', {'post': post}, {'form': form})

def comollegar(request):
    return render(request, 'comollegar.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'