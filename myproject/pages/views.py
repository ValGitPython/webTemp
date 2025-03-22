from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'pages/home.html', {'content': 'Добро пожаловать на главную страницу!'})

def data_view(request):
    return render(request, 'pages/data.html', {'content': 'Это страница DATA'})

def test_view(request):
    return render(request, 'pages/test.html', {'content': 'Это страница TEST'})