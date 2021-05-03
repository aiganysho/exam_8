from django import forms
from webapp.models import Product, Review

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'category', 'description', 'picture')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text_review', )
        exclude = ('moderation', )