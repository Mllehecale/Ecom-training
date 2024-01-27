from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    # date ajoutée automatiquement quand instance de category crée

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_added']  # ici on ordonne les produits selon ajout

    def __str__(self):
        return self.title

class Commande(models.Model):
    items=models.CharField(max_length=300)
    nom=models.CharField(max_length=150)
    email=models.EmailField()
    adresse=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    pays=models.CharField(max_length=300)
    zip=models.CharField(max_length=300)
    date_commande=models.DateTimeField(auto_now=True)
    total=models.CharField(max_length=200)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom  # retourne le nom de l'utilisateur qui a passé commande


