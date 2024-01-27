from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Product, Commande


# Create your views here.

def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)  # affiche tout ce qui contient ce mot
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total=request.POST.get('total')
        nom = request.POST.get("nom")
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zip = request.POST.get('zip')
        com = Commande(items=items,total=total,nom=nom, email=email, adresse=adresse, ville=ville, pays=pays, zip=zip)
        com.save()

    return redirect('confirmation') #ici cest le nom qu'on prend

def confirmation(request):
    info=Commande.objects.all()[:1]
    for item in info:
        nom=item.nom #ici on récupère uniquement le nom

    return render(request,'shop/confirmation.html', {'name':nom})