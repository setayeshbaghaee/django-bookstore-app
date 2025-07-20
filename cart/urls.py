
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>', views.cart_detail_view, name='cart'),
    
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_Item'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
    path('add/<int:pk>/', views.ItemCreateView.as_view(), name='add'),

    path('checkout/<int:pk>/', views.UserView.as_view(), name='checkout'),

] 
