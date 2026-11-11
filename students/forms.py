from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "department"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter student name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "department": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter department"}),
        }
