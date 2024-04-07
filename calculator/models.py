from django.db import models

CONSUMER_TYPE_CHOICES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    ]

class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    #  create the foreign key for discount rule model here


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""
class DiscountRules(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    consumer_type = models.CharField("Tipo de Consumidor", max_length=128, choices=CONSUMER_TYPE_CHOICES)

    consumption_range = models.IntegerField("Faixa de Consumo")

    cover_value = models.IntegerField("Valor da Cobertura")

    distributor_tax = models.FloatField("Tarifa da Distribuidora", default=0.0)

    discount_value = models.FloatField("Valor do Desconto")


# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
