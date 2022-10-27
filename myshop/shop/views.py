from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Получение списка продуктов
def product_list(request, category_slug=None):
    category = None
    # Получаем все категории товаров
    categories = Category.objects.all()
    # получаем все товары при этом фильтруем по коонке "доступность"
    products = Product.objects.filter(available=True)
    # Если получили в запросе category_slug вытаскиваем все продукты нужной категории 
    if category_slug:
        # Получаем категорию
        category = get_object_or_404(Category, slug=category_slug)
        # получаем продукты указанной категории
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

# Получение одного продукта
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})