from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from plat.forms import PlatForm
from plat.models import PlatModel

# Create your views here.
def edit_plat(request):
    if request.method == 'POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pages:plats')
    
    form = PlatForm()
    return render(request, 'pages/edit_plat.html', {'form': form})

def update_plat(request, pk):
    plat_id = PlatForm.objects.get(id=pk)
    form = PlatForm(instance=plat_id)
    
    if request.method == "POST":
        form =PlatForm(request.POST, instance=plat_id)
        if form.is_valid():
            form.save()
        return redirect('pages:plats')  # Rediriger après une mise à jour réussie

    context = {'form': form}
    return render(request, 'pages/update_plat.html', context)

def delete_plat(request, pk):
    plat = get_object_or_404(PlatModel, pk=pk)
    if request.method == 'POST':
        plat.delete()
        return redirect('pages:plats')  # Rediriger après une suppression réussie

    return render(request, 'pages/delete_plat.html', {'plat': plat})

def plats(request):
    plat = PlatModel.objects.all()
    return render(request, 'pages/plats.html', {'plat': plat})