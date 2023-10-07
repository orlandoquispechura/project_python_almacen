from django import forms
from .models import Product, Category
from .validators import max_name, price_min, stock_min


class ProductForm(forms.ModelForm):
    # category = forms.Select(validators=[required_category])

    class Meta:
        model = Product
        fields = "__all__"

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), validators=[max_name]
    )
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        validators=[stock_min],
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        validators=[price_min],
    )
    status = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select"},
        ),
    )
