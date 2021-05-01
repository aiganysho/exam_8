from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.form import ProductForm
from django.shortcuts import reverse
from django.urls import reverse_lazy


class ProductList(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'product_list'


class ProductDetail(DetailView):
    template_name = 'product/view_product.html'
    context_key = 'product'
    model = Product


class ProductCreate(CreateView):
    template_name = 'product/create_product.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse(
            'product:view',
            kwargs={'pk': self.object.pk}
        )



class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product/update_product.html'
    form_class = ProductForm
    context_key = 'product'

    def get_success_url(self):
        return reverse(
            'product:view',
            kwargs={'pk': self.object.pk}
        )

class ProductDelete(DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    context_key = 'product'
    success_url = reverse_lazy('product:list')
