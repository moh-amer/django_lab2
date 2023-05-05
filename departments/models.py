from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=100, null=False, blank=False)


    @classmethod
    def get_all_departments(cls):
        return cls.objects.all()

    @classmethod
    def get_department_by_id(cls, id):
        return cls.objects.get(id=id)


    def delete_department(self):
        self.delete()

    def get_delete_url(self):
        return reverse("departments.delete", args=[self.id])

    def get_insert_department_url(self):
        return reverse("departments.insert")

    def get_update_department_url(self):
        return reverse("departments.update", args=[self.id])

    def get_show_department_url(self):
        return reverse("departments.show", args=[self.id])

    def __str__(self):
        return self.dept_name