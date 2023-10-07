from django.urls import path, include
from .views import categorias, productos, productoFormView
from .views import CategoryViewSet
from .views import ProductViewSet
from .views import CustomerViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r"categorias", CategoryViewSet)
router.register(r"productos", ProductViewSet)
router.register(r"clientes", CustomerViewSet)


urlpatterns = [
    # ruta para crear/ listar categorias, productos
    # path("categorias/", categorias, name="categorias"),
    # path("productos/", productos, name="productos"),
    # path("productos/", productoFormView, name="productos"),


    # ruta Api ModelViewSet categorias, productos, clientes
    path("", include(router.urls)),
]
