from django.shortcuts import render

def about(request):
    """Страница 'О проекте'."""
    return render(request, 'about.html')

def rules(request):
    """Страница 'Правила'."""
    return render(request, 'rules.html')