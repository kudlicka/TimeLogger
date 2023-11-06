from django.shortcuts import render, get_object_or_404
from .models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, "index.html", {"employees": employees})


def employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "employee.html", {"employee": employee})
