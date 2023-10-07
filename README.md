# project_python_almacen
proyecto realizado en python django rest framewrok modulo almacén 

# rutas de 3 modelos 
router = routers.SimpleRouter()
router.register(r"categorias", CategoryViewSet)
router.register(r"productos", ProductViewSet)
router.register(r"clientes", CustomerViewSet)

  # ruta para crear/ listar categorias, productos
    # path("categorias/", categorias, name="categorias"),
    path("productos/", productos, name="productos"),

  # ruta para crear/listar productos y validaciones 
    path("productos/", productoFormView, name="productos"),

   # ruta Api ModelViewSet categorias, productos, clientes
    path("", include(router.urls)),

# ruta para buscar los productos de una categoria específica según el id
  ejem: ruta de api=>  http://127.0.0.1:8000/almacen/productos/?category=1
