from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from .views import user_login , user_register,user_logout , UserDetailView , UserUpdateView

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', UserUpdateView.as_view(), name='update_profile'),

]
