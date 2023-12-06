from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout

# Create your views here.

'''Главная страница сайта'''
def index(request):
    data = {'header': 'Главная страница сайта',
            'text1': 'Компания "Сельхозмаркет" занимается реализацией сельхозтехники, продажей запчастей и комплектующих в хозяйства РФ и страны СНГ.',
            'list': ['Работаем по России и СНГ', 'При необходимости организуем доставку до клиента', 'Особые условия для постоянных клиентов','Гарантия на товары','Большой ассортимент','Реализуем товар оптом и в розницу'],
            }
    return render(request, 'example_app/index.html', context=data)


'''Страница Контакты'''
def contact(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            appeal = userform.cleaned_data['appeal']
            data = {'header': 'Контакты',
                    'list': ['Тел(WhatsApp): +7-908-202-40-65', 'E-mail: fortagro@list.ru', 'Адрес: г. Красноярск, ул. Шахтеров, склад 10'],
                    'map': 'https://yandex.ru/map-widget/v1/?ll=92.887918%2C56.026812&mode=search&sll=92.889340%2C56.027190&text=56.027190%2C92.889340&z=17.18%27',
                    'answare': f'Мы приняли Ваше обращение:<br>{appeal}<br><br> B ближайшее время мы с Вами свяжемся.'  # переменная для вывода ответа на этой же странице
                    }
        #return HttpResponse('Ошибка при передаче данных!<br>Свяжитесь с нами по телефону') если ответ на отдельной странице
        else:
            data = {'header': 'Контакты',
                    'list': ['Тел(WhatsApp): +7-908-202-40-65', 'E-mail: fortagro@list.ru', 'Адрес: г. Красноярск, ул. Шахтеров, склад 10'],
                    'map': 'https://yandex.ru/map-widget/v1/?ll=92.887918%2C56.026812&mode=search&sll=92.889340%2C56.027190&text=56.027190%2C92.889340&z=17.18%27',
                    'answare': 'Ошибка при передаче данных!<br>Свяжитесь с нами по телефону'
                    }
        return render(request, 'example_app/contact.html', context=data)
    else:
        form = UserForm()  # переменная для формы
        data = {'header': 'Контакты',
                'list': ['Тел(WhatsApp): +7-908-202-40-65', 'E-mail: fortagro@list.ru',
                'Адрес: г. Красноярск, ул. Шахтеров, склад 10'],
                'map': 'https://yandex.ru/map-widget/v1/?ll=92.887918%2C56.026812&mode=search&sll=92.889340%2C56.027190&text=56.027190%2C92.889340&z=17.18%27',
                'header_form': 'Форма для обращения в техподдержку:',
                'form': form,
                'submit': "<input class='btn btn-danger' type = 'submit' value = 'Отправить'>"}
    return render(request, 'example_app/contact.html', context=data)


'''Страница Товары'''
def products(request):
    product = Product.objects.all()
    print(product)  # вывод продукта в консоль
    data = {'header': 'Товары',
            'list': [],
            'product': product,
            }
    return render(request, 'example_app/products.html', context=data)


'''Страница Склад'''
def stock(request):
    product = Product.objects.all()
    print(product) # вывод продукта в консоль
    productForm = ProductForm()  # переменная для вывода формы на странице сайта из файла forms.py

    supplier = Supplier.objects.all()
    print(supplier)
    supplierForm = SupplierForm()

    stock = Stock.objects.all()
    print(stock)
    stockForm = StockForm()

    data = {'header': 'Склад',
            'list': [],
            'product':product,
            'supplier': supplier,
            'stock': stock,
            'productForm': productForm,
            'supplierForm': supplierForm,
            'stockForm': stockForm,
            }
    return render(request, 'example_app/stock.html', context=data)


'''Описание формы для получения данных товара'''
def products_create(request):
    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
        else:
            print('Не корректные данные!')
        return HttpResponseRedirect('/stock')
    return HttpResponseRedirect('/stock')


'''Описание формы для получения данных поставщика'''
def supplier_create(request):
    if request.method == 'POST':
        supplier = SupplierForm(request.POST)
        if supplier.is_valid():
            supplier.save()
        else:
            print('Не корректные данные!')
        return HttpResponseRedirect('/stock')
    return HttpResponseRedirect('/stock')


'''Описание формы для добавления товара на склад'''
def stock_add(request):
    if request.method == 'POST':
        stock = StockForm(request.POST)
        if stock.is_valid():
            stock.save()
        else:
            print('Не корректные данные!')
        return HttpResponseRedirect('/stock')
    return HttpResponseRedirect('/stock')


'''Страница Сделки'''
def deal(request):
    deal = Deal.objects.all()
    data = {'header': 'Сделки',
            'deal': deal,
            }
    return render(request, 'example_app/deal.html', context=data)


'''Описание формы аутентификации'''
def login_view(request):
    form = LoginForm()
    data = {'header': 'Вход и регистрация', 'form': form}
    if request.method=='POST':
        userform = LoginForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['login'] # информация из поля логин
            password = userform.cleaned_data['password'] # информация из поля пароль
            print(username, password) # вывод для себя
            user = authenticate(username=username, password=password) # вызываем функцию аутентификации для проверки, передаем в нее даанные
            print('user=', user) # вывод для себя
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/deal') # переходим на страницу Cделки
        data = {'header': 'Вход и регистрация', 'form': form, 'answare':'Не корректные данные, введите логин и пароль!'}
        return render(request, 'example_app/login.html', context=data)
    return render(request, 'example_app/login.html', context=data)


'''Функция для выхода из личного кабинета'''
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/') # переходим на главную страницу