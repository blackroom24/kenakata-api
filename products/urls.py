from django.urls import path
from products import views

urlpatterns = [
    path("collections/", views.AllCategories.as_view()),
    path("collections/allproducts", views.AllProducts.as_view()),
    path("collections/<slug:category_slug>/", views.CategoryDetail.as_view()),
    path(
        "collections/<slug:category_slug>/<slug:product_slug>/",
        views.ProductDetail.as_view(),
    ),
    path("search/", views.search),
]
