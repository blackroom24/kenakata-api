from django.urls import path, include
from products import views

urlpatterns = [
    path("product-list/", views.ProductList.as_view()),
]
