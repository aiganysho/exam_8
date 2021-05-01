from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class RegisterView(CreateView):
    model = User
    template_name = 'registration/user_create.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('product:list')
        return next_url
