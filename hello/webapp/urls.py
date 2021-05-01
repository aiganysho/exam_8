from django.urls import path
from webapp.views import (
    ProductList,
    ProductDetail,
    ProductCreate,
    ProductUpdate,
    ProductDelete
)


app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<int:pk>', ProductDetail.as_view(), name='view'),
    path('product/add/', ProductCreate.as_view(), name='create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),

]