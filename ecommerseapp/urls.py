from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove/<int:id>/', views.remove_cart_item, name='remove'),
    # path("checkout/<int:id>/", views.checkout, name="checkout"),
    path("place_order/<int:id>/", views.place_order, name="place_order"),
    path("order-page/", views.oderPage, name='orderPage'),

]