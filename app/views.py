from django.shortcuts import render, redirect
from app.forms import UsuariosForm
from app.models import Usuarios
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    all_usuarios = Usuarios.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        data['search_query'] = search_query
        data['db'] = Usuarios.objects.filter(nome__icontains=search_query)
        

    else:
        paginator = Paginator(all_usuarios, 3)
        page_number = request.GET.get('page')
        data['db'] = paginator.get_page(page_number)

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = UsuariosForm()
    return render(request, 'form.html', data)

def create(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
        data = {}
        data['db'] = Usuarios.objects.get(pk=pk)
        return render(request, 'view.html', data)

def edit(request, pk):
        data = {}
        data['db'] = Usuarios.objects.get(pk=pk)
        data['form'] = UsuariosForm(instance=data['db'])
        return render(request, 'form.html', data)

def update(request, pk):
        data = {}
        data['db'] = Usuarios.objects.get(pk=pk)
        form = UsuariosForm(request.POST or None, instance=data['db'])
        if form.is_valid():
            form.save()
            return redirect('home')
        
def delete(request, pk):
        db = Usuarios.objects.get(pk=pk)
        db.delete()
        return redirect('home')