from django.shortcuts import render
from .utils import AverageCalculator


# Create your views here.
def home(request):
    result = None
    if request.method == 'POST':
        grades = request.POST.getlist('grades')
        weights = request.POST.getlist('weights')
        action = request.POST.get('action')
        
        calculator = AverageCalculator(grades, weights)
        
        if action == 'calculate':
            result = calculator.calculate()

        elif action == 'needed-grade':
            result = calculator.grade_to_Approve()

        else:
            result = "Acción no reconocida. Por favor, intente de nuevo."

        
    return render(request, 'promedio.html', {'result': result})