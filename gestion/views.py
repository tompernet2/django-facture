from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Facture, LigneFacture
from .forms import ProduitForm 
from django.core.paginator import Paginator
from django.contrib import messages




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
            return redirect('liste_produits')  
    else:
        form = ProduitForm()
    return render(request, 'gestion/produit_form.html', {'form': form})


def produit_delete(request, pk):
    produit = Produit.objects.get(id=pk) 
    produit.delete()  
    return redirect('liste_produits')  


def produit_update(request, pk):
    produit = Produit.objects.get(id=pk)  

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)  
        if form.is_valid():
            form.save() 
            return redirect('liste_produits')  
    else:
        form = ProduitForm(instance=produit) 

    return render(request, 'gestion/update_form.html', {'form': form})

def produits_facture(request):
    produits = Produit.objects.all()
    return render(request, "gestion/produits_facture.html", {"produits": produits})


def facture_create(request):
    if request.method == "POST":
        produits_ids = request.POST.getlist('produits_selectionnes')  

        if not produits_ids:
            messages.error(request, "Veuillez sélectionner au moins un produit.")
            return redirect('produits_facture')  

        facture = Facture.objects.create()

        for prod in produits_ids:
            produit = Produit.objects.get(id=prod)
            LigneFacture.objects.create(
                facture=facture,
                nom=produit.nom,
                prix=produit.prix,
                date_peremption=produit.date_peremption,
            )

        return redirect('facture_detail', pk=facture.id)

    return redirect('produits_facture')

def facture_detail(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'gestion/facture_detail.html', {'facture': facture})


def liste_factures(request):
    factures_list = Facture.objects.order_by('-date') 
    paginator = Paginator(factures_list, 4)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gestion/liste_factures.html', {'page_obj': page_obj})