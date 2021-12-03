from django.urls import path, include
from products import views

urlpatterns = [
    path("product-list/", views.ProductList.as_view()),
    path("products/<slug:category_slug>/", views.CategoryDetail.as_view()),
    path(
        "products/<slug:category_slug>/<slug:product_slug>/",
        views.ProductDetail.as_view(),
    ),
]
