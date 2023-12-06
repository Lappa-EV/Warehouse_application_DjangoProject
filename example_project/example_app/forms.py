from django import forms
from django.forms import ModelForm   # для создания формы на основе модели
from.models import*  # для создания формы на основе модели


class UserForm(forms.Form):
    name = forms.CharField(label='Введите Ф.И.О:', min_length=9)
    number = forms.IntegerField(label='Введите номер отдела:', initial=1, max_value=4, min_value=1, widget=forms.NumberInput)
    appeal = forms.CharField(label='Опишите проблему:', min_length=8, widget=forms.Textarea)


'''Описание переменных формы номентклатуры товара'''
class ProductForm(forms.ModelForm):# формa на основе модели
    class Meta:
        model = Product
        fields = ['name','description','type','аggregation']


'''Описание переменных формы номентклатуры поставщика'''
class SupplierForm(forms.ModelForm): # формa на основе модели
    class Meta:
        model = Supplier
        fields = ['name']


'''Описание переменных формы добавления товара на склад'''
class StockForm(forms.ModelForm): # формa на основе модели
    class Meta:
        model = Stock
        fields = ['product', 'supplier', 'delivery_price', 'quantity_product','delivery_date']


'''Описание переменных формы аутентификации'''
class LoginForm(forms.Form):
    login = forms.CharField(max_length=10, label='Логин:', widget = forms.TextInput(attrs={'type':'text'}))
    password = forms.CharField(max_length = 20, label='Пароль:', widget = forms.TextInput(attrs={'type': 'password'}))
