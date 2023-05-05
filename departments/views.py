from django.shortcuts import render, redirect
from .models import Department
from employees.models import Employee
from .forms import DepartmentForm

# Create your views here.
def get_departments(request):
    departments = Department.get_all_departments()
    return render(request, "departments/index.html", context={"depts": departments})

def show_department(request, id):
    department = Department.get_department_by_id(id)
    if(department):
        employees = Employee.get_all_employees_from_department(department)
        return render(request, "departments/show-department.html", context={"dept": department, "emps": employees})
    else:
        return render(request, "departments/notfound.html")

def delete_department(request, id):
    department = Department.get_department_by_id(id)
    if(department):
        department.delete_department()
        return redirect("departments.getdepts")

def insert_department(request):
    form = DepartmentForm()
    if request.method == "GET":
        return render(request, "departments/insert.html", context={"form": form})
    else:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departments.getdepts")
        else:
            return redirect("departments.insert")

def update_department(request, id):
    department = Department.get_department_by_id(id)
    form = DepartmentForm(instance=department)
    if request.method == "GET":
        return render(request, "departments/update.html", context={"form": form})
    else:
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        return redirect("departments.getdepts")