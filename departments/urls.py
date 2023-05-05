from django.urls import path
from .views import get_departments, delete_department, show_department, update_department, insert_department


urlpatterns = [
    path('', get_departments, name="departments.getdepts"),
    path('delete/<int:id>', delete_department, name="departments.delete"),
    path('show/<int:id>', show_department, name="departments.show"),
    path('update/<int:id>', update_department, name="departments.update"),
    path('insert', insert_department, name="departments.insert"),
]