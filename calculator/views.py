from django.http import HttpResponse
from django.shortcuts import render
from calculator.forms import CalculatorForm
from calculator.models import Consumer, DiscountRules
from calculator_python import calculator
import openpyxl

# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    # Create the first view here.

    # workbook = openpyxl.load_workbook("consumers.xlsx")
    # sheet = workbook["Sheet1"]

    # for row in sheet.iter_rows(min_row=2,values_only=True): 
        # consumer = Consumer(
        # name=row[1],
        # document=row[2],
        # city=row[3],
        # state=row[4],
        # )
        # consumer_id = row[0]
        # discount = calculator([row[5]], row[8], row[6])  
        # discountRule = DiscountRules(
        #     consumer_id=consumer_id,
        #     consumer_type=row[6],
        #     consumption_range=row[5],
        #     cover_value=row[7],
        #     distributor_tax=row[8],
        #     discount_value= discount[1]
        # )
        # discountRule.save()
        # consumer.save()


    consumers = Consumer.objects.all()
    discountRules = DiscountRules.objects.all()
    context = {"consumers": consumers, "discount": discountRules }
    return render(request, "calculator/list.html", context)









# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2(request):
    # Create the second view here.
    
    if request.method == 'GET':
        form = CalculatorForm()
        return render(request, 'calculator/calculator.html', {'form': form})
    elif request.method == 'POST':
        data = request.POST
        arrayNumbers = [int(data['number1']), int(data['number2']), int(data['number3'])]
        
        calculatorResult = calculator(arrayNumbers, float(data['distributor_tax']), data['tax_type'])
        
        
        form = CalculatorForm()
        print(calculatorResult)
        context = {
            'form': form,
            'annual_savings': calculatorResult[0],
            'monthly_savings': calculatorResult[1],
            'discount_rate': calculatorResult[2],
            'coverage': int(calculatorResult[3] * 100),
            'result': True
            }
        return render(request, 'calculator/calculator.html', context)
       