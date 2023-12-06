from django.db import models
from django.contrib.auth.models import User


'''Товар'''
class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='Нименование товара',)
    description = models.CharField(max_length=1000, verbose_name='Описание товара')
    type = models.CharField(max_length=50, verbose_name='Тип устройства')
    аggregation = models.CharField(max_length=500, verbose_name='Агрегатирование')
    def __str__(self):  # чтобы при выборе группы виделось только имя
        return self.name


'''Поставщик'''
class Supplier(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название компании-поставщика')
    def __str__(self):
        return self.name


'''Склад'''
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  verbose_name='Товар', null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,  verbose_name='Поставщик', null=True)
    delivery_date = models.DateField(default='2023-01-01', verbose_name='Дата поставки')
    delivery_price = models.IntegerField(max_length=20,verbose_name='Цена ед. товара, руб')
    quantity_product = models.IntegerField(verbose_name='Количество товара, шт')
    def __str__(self):
        return str(self.product)


'''Таблица сделка'''
class Deal(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField(verbose_name='Дата сделки')
    quantity = models.IntegerField(verbose_name='Количество проданного товара, шт')
    delivery_price = models.IntegerField(max_length=20,verbose_name='Цена ед. товара, руб')
    def __str__(self):
        return str(self.date) +' / '+ str(self.product) +' / '+ str(self.quantity)+' шт. / '+ str(self.delivery_price)+' руб. / сотрудник: '+ str(self.employee)
