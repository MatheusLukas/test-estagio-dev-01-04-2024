from django.db import models


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
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
    CONSUMER_TYPE_CHOICES = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
    ]

    CONSUMPTION_RANGE_CHOICES = [
        ('0-100', '0-100'),
        ('101-200', '101-200'),
        ('201-300', '201-300'),
        ('301-400', '301-400'),
        ('401-500', '401-500'),
        ('501-600', '501-600'),
        ('601-700', '601-700'),
        ('701-800', '701-800'),
        ('801-900', '801-900'),
        ('901-1000', '901-1000'),
    ]

    consumer_type = models.CharField("Tipo de Consumidor", max_length=128, choices=CONSUMER_TYPE_CHOICES)
    consumption_range = models.CharField("Faixa de Consumo", max_length=128, choices=CONSUMPTION_RANGE_CHOICES)
    cover_value = models.FloatField("Valor da Cobertura")
    discount_value = models.FloatField("Valor do Desconto")

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
