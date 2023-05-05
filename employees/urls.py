from django.urls import path
from .views import getemps,show_employee_details, insert_employee, delete_employee, update_employee

urlpatterns = [
    path('', getemps, name="employees.getemps"),
    path('show/<int:id>', show_employee_details, name="employees.show"),
    path('insert', insert_employee, name="employees.insert"),
    path('delete/<int:id>', delete_employee, name="employees.delete"),
    path('update/<int:id>', update_employee, name="employees.update"),
]
