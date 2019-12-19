from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Record
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RecordList(LoginRequiredMixin, ListView):
    model = Record

class RecordDetail(LoginRequiredMixin, DetailView):
    model = Record

class RecordCreate(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['album_name', 'artist', 'year', 'label', 'condition']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class RecordUpdate(LoginRequiredMixin, UpdateView):
  model = Record
  fields = ['album_name', 'artist', 'year', 'label', 'condition']

class RecordDelete(LoginRequiredMixin, DeleteView):
  model = Record
  success_url = '/records/'