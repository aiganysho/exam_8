from django.urls import path
from webapp.views import (
    ProductList,
    ProductDetail,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    ReviewList,
    ReviewCreate,
    ReviewUpdate,
    ReviewDelete,
    ReviewDetail
)


app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<int:pk>', ProductDetail.as_view(), name='view'),
    path('product/add/', ProductCreate.as_view(), name='create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/review/', ReviewList.as_view(), name='list_review'),
    path('<int:pk>/review/create/', ReviewCreate.as_view(), name='create_review'),
    path('<int:pk>/review/update/', ReviewUpdate.as_view(), name='update_review'),
    path('<int:pk>/review/delete/', ReviewDelete.as_view(), name='delete_review'),
    # path('<int:pk>/review/detail/', ReviewDelete.as_view(), name='detail_review'),

]