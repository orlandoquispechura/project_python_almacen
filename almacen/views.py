from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer
from .models import Category, Product, Customer
from .forms import ProductForm

# Create your views here.


def categorias(request):
    post_name = request.POST.get("name")
    post_description = request.POST.get("description")

    try:
        if post_name and post_description:
            category = Category(name=post_name, description=post_description)
            category.save()
    except:
        print("llenar datos")
    filter_name = request.GET.get("name")
    if filter_name:
        categories = Category.objects.filter(nombre_regex=f"{filter_name}$")
    else:
        categories = Category.objects.all()

    return render(request, "form_categorias.html", {"categorias": categories})


def productos(request):
    categorias = Category.objects.all()

    post_name = request.POST.get("name")
    post_stock = request.POST.get("stock")
    post_price = request.POST.get("price")
    post_category = request.POST.get("category_id")

    try:
        if post_name and post_stock and post_price and post_category:
            producto = Product(
                name=post_name,
                stock=post_stock,
                price=post_price,
                category_id=post_category,
            )
        producto.save()
    except:
        print("Faltan datosde producto")
    productos = Product.objects.all()
    return render(
        request,
        "form_productos.html",
        {"productos": productos, "categorias": categorias},
    )


# ModelForm product
def productoFormView(request):
    productos = Product.objects.all()

    form = ProductForm(request.POST)
    try:
        if form.is_valid():
            form.save()
    except:
        print("faltan datos")
    return render(
        request, "form_productos.html", {"form": form, "productos": productos}
    )


# serializers ModelViewSet Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer


# serializers ModelViewSet Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer

    # funcion para el filtrado de productos segun el Id de una categoria
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset


# serializers ModelViewSet Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("-id")
    serializer_class = CustomerSerializer
