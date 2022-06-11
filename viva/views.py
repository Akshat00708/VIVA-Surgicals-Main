from django.shortcuts import render


def main(request):
    return render(request, "main.html")

def product(request):
    return render(request, 'product.html')
