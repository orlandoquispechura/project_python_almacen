from django.core.exceptions import ValidationError


# funcion para validar que el precio no sea ingresado en negativo
def price_min(value):
    if value < 0:
        raise ValidationError("No se aceptan números negativos")


# funcion para validar que el stock de producto no sea ingresado en negativo
def stock_min(value):
    if value < 0:
        raise ValidationError("Stock no se aceptan números negativos")


# funcion para validar que categoria en la tabla producto sea requerido
def required_category(value):
    if value == None:
        raise ValidationError("El campo categoria es requerido")


# funcion para validar el campo nombre no sea mayor a lo requerido en el Modelo Product
def max_name(value):
    longitud = len(value)
    if longitud> 100:
        raise ValidationError(f"No debe pasar de los 100 caracteres, caracteres digitados : {longitud}")
