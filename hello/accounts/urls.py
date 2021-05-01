from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from accounts.views import RegisterView



app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create')

]