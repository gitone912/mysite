from django import forms
 
class Userform(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
    paass=forms.PasswordInput()