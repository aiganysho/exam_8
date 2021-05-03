from webapp.models import Review
from webapp.form import ReviewForm, Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Avg





class ReviewList(ListView):
    template_name = 'product/index.html'
    model = Review
    context_object_name = 'review_list'


class ReviewCreate(CreateView):
    template_name = 'product/create_product.html'
    form_class = ReviewForm
    model = Review

    def get_success_url(self):
        return reverse(
            'product:view',
            kwargs={'pk': self.object.pk}
        )

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))

        review = form.instance
        review.product = product
        review.author = self.request.user

        return super().form_valid(form)
    #
    #
    # def get_avg(self):
    #     context = Review.objects.filter(product=self).aggregate(average=Avg('rate'))
    #     avg = 0
    #     if context['average'] is not None:
    #         avg = float(context['average'])
    #         return avg
    #     context['average'] = context
    #     return context




class ReviewUpdate(UpdateView):
    model = Review
    template_name = 'product/update_product.html'
    form_class = ReviewForm
    context_key = 'review'

    def get_success_url(self):
        return reverse(
            'product:view',
            kwargs={'pk': self.object.pk}
        )

class ReviewDelete(DeleteView):
    template_name = 'product/delete_product.html'
    model = Review
    context_key = 'review'
    success_url = reverse_lazy('product:view')

