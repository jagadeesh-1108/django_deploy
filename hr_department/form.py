from django import forms

from hr_department.models import emp_table

class employee_form(forms.ModelForm):
    class Meta:
        model = emp_table
        fields = "__all__"

