from django import forms
from calculator.models import CONSUMER_TYPE_CHOICES


class CalculatorForm(forms.Form):
    number1 = forms.IntegerField(label='Primeiro mês' ,widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}), label_suffix=" (R$):")
    number2 = forms.IntegerField(label='Segundo mês',widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}), label_suffix=" (R$):")
    number3 = forms.IntegerField(label='Terceiro mês',widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}), label_suffix=" (R$):")
    distributor_tax = forms.FloatField(label='Tarifa da Distribuidora',widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}))
    tax_type = forms.ChoiceField(label='Tipo de Consumidor', choices=CONSUMER_TYPE_CHOICES)





     