from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from.models import order,employee

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")
        if p1 != p2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class orderForm(forms.ModelForm):
    class Meta:
        model=order
        fields=['your_name','email','phone','your_destination','av_name','product_price','image','date_order']
class employeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields = [
            'fist_name',
            'las_name',
            'tel',
            'national_id',
            'email',
            'joinig_date',
            'photos',
            'salary',
            'dept_name'
        ]


