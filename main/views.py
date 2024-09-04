from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306222746',
        'name': 'Pascal Hafidz Fajri',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)