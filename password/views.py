from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry
from .forms import PasswordEntryForm
import random
letters_list = ['a', 'b', 'A', 'B']
numbers_list = ['1', '2', '3', '4']
symbols_list = ['#', '$', '%', '&', '*', '?']

def password_list(request):
    kerakli_royhatlar = []
    password = []
    length = request.GET.get("length",0)
    
    letters = request.GET.get('letters')
    symbols = request.GET.get("symbols")
    number = request.GET.get('numbers')
    if letters:
        kerakli_royhatlar.append(letters_list)
    if symbols:
        kerakli_royhatlar.append(symbols_list)
    if number:
        kerakli_royhatlar.append(numbers_list)
    if kerakli_royhatlar:
        for i in range(int(length)):
            royhat = random.choice(kerakli_royhatlar)
            belgi = random.choice(royhat)
            password.append(belgi)
    
    password = "".join(password)
    return render(request, 'index.html', {'password': password, 'length':length, 'letters':letters, 'symbols':symbols, 'number':number})

