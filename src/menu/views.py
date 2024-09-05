from django.shortcuts import get_object_or_404, redirect, render

from menu.forms import MenuForm
from menu.models import MenuModel

# Create your views here.
def edit_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pages:menus')
    
    form = MenuForm()
    return render(request, 'pages/edit_menu.html', {'form': form})

def update_menu(request, pk):
    menu_id = MenuForm.objects.get(id=pk)
    form = MenuForm(instance=menu_id)
    
    if request.method == "POST":
        form =MenuForm(request.POST, instance=menu_id)
        if form.is_valid():
            form.save()
        return redirect('pages:menus')  # Rediriger après une mise à jour réussie

    context = {'form': form}
    return render(request, 'pages/update_menu.html', context)

def delete_menu(request, pk):
    menu = get_object_or_404(MenuModel, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('pages:menus')  # Rediriger après une suppression réussie

    return render(request, 'pages/delete_menu.html', {'menu': menu})

def menus(request):
    menu = MenuModel.objects.all()
    return render(request, 'pages/menus.html', {'menu': menu})