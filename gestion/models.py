from django.db import models

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(ligne.prix for ligne in self.lignes.all())

    def nombre_produits(self):
        return self.lignes.count()

    def __str__(self):
        return f"Facture #{self.id} - {self.date.strftime('%d/%m/%Y')}"


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return f"{self.nom} - {self.prix} €"
