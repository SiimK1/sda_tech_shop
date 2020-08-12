from django.urls import path, include
from estore.views import HomeView, CategoryView, CheckoutView, CartView, ContactView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('Categories/', CategoryView.as_view(), name="Category"),
    path('Checkout/', CheckoutView.as_view(), name="Checkout"),
    path('Cart/', CartView.as_view(), name="Cart"),
    path('Contact/', ContactView.as_view(),  name="Contact"),
    path('Product/', ProductView.as_view(), name="Product"),

]
