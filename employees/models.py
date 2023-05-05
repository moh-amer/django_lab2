from django.db import models
from django.shortcuts import reverse
from departments.models import Department

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200,null=False, blank=True)
    age = models.IntegerField(max_length=60, null=False, default=18)
    salary = models.FloatField(max_length=20, blank=False, null=False, default=0.0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    @classmethod
    def get_all_employees(cls):
        return cls.objects.all()

    @classmethod
    def get_employee_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_all_employees_from_department(cls, department):
        return cls.objects.filter(department=department)


    def delete_employee(self):
        self.delete()

    def get_show_url(self):
        return reverse('employees.show', args=[self.id])

    def get_delete_url(self):
        return reverse('employees.delete', args=[self.id])

    def get_update_url(self):
        return reverse('employees.update', args=[self.id])

    def __str__(self):
        return self.name