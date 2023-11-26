from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.index, name='index'),
  # APIView Menu
  path('menu/', views.MenuView.as_view()),
  path('booking/', views.BookingView.as_view()),

  # Generic View Menu
  path('menu-items/', views.MenuItemView.as_view()),
  path('menu-item/<int:pk>/', views.SingleItemView.as_view()),

  # Secure View
  path('secret-view/', views.secure_view),
  path('secure-menu-items/', views.MenuItemsViewWithAuth.as_view()),

  # Generating Auth Token
  path('api-token-auth', obtain_auth_token),
]