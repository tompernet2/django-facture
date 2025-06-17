from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Facture
from .forms import ProduitForm 
from django.core.paginator import Paginator



def liste_produits(request):
    produits = Produit.objects.all().order_by('id')
    paginator = Paginator(produits, 4)

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'gestion/liste_produits.html', {'page_obj': page_obj})


def produit_create(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit_list')  
    else:
        form = ProduitForm()
    return render(request, 'gestion/produit_form.html', {'form': form})


def produit_delete(request, pk):
    produit = Produit.objects.get(id=pk) 
    produit.delete()  
    return redirect('produit_list')  


def produit_update(request, pk):
    produit = Produit.objects.get(id=pk)  

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)  
        if form.is_valid():
            form.save() 
            return redirect('produit_list')  
    else:
        form = ProduitForm(instance=produit) 

    return render(request, 'gestion/update_form.html', {'form': form})