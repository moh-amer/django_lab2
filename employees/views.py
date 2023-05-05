from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Employee
from .forms import EmpForm

# Create your views here.


employees = ["Mohamed","Ahmed", "Ali", "Hossam"]
def getemps(request):
    employees = Employee.get_all_employees()
    return render(request, 'employees/employees.html', context={"emps": employees})
def show_employee_details(request, id):
    employee = Employee.get_employee_by_id(id)
    return render(request, 'employees/show-emp.html', context={"emp": employee})

def delete_employee(request, id):
    employee = Employee.get_employee_by_id(id)
    if employee:
        employee.delete_employee()
        return redirect(reverse("employees.getemps"))



def update_employee(request, id):
    employee = Employee.get_employee_by_id(id)
    if request.method == "GET":
        form = EmpForm(instance=employee)
        return render(request, "employees/update.html", context={"form":form})
    else:
        form = EmpForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect(reverse("employees.show", args=[id]))


def insert_employee(request):
    form = EmpForm()
    if request.method == "GET":
        return render(request, "employees/insert.html", context={"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()

        # url = reverse("employees.getemps")
        return redirect(reverse("employees.getemps"))