from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import InteracaoForm
from app.models import Interacao
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    data ['db'] = Interacao.objects.all()
    all = Interacao.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data ['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = InteracaoForm()
    return render(request, 'form.html', data)

def create(request):
    form = InteracaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Interacao.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Interacao.objects.get(pk=pk)
    data['form'] = InteracaoForm(instance=data['db'])
    return render (request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Interacao.objects.get(pk=pk)
    form = InteracaoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Interacao.objects.get(pk=pk)
    db.delete()
    return redirect('home')