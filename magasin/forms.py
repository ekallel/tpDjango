from django import forms
from django.forms import ModelForm 
from .models import Produit 
from .models import Fournisseur ,Commande,Categorie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduitForm(ModelForm):
     class Meta : 
        model = Produit
        fields = "__all__" #pour tous les champs de la table
        #fields=['libellé','description']  #pour qulques champs
class FournisseurForm(ModelForm):
     class Meta : 
        model = Fournisseur
        fields = "__all__" #pour tous les champs de la table

class UserRegistrationForm(UserCreationForm):
      first_name = forms.CharField(label='Prénom')
      last_name = forms.CharField(label='Nom')
      email = forms.EmailField(label='Adresse e-mail')
      class Meta(UserCreationForm.Meta):
         model = User
         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class CommandeForm(forms.ModelForm):
    produits = forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = Commande
        fields = '__all__'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__" 