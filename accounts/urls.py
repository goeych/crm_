
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),

    
    path('', views.home,name='home'),
    path('user/',views.userPage,name='userPage'),
    path('accountsetting/',views.accountSettings,name='accountSettings'),
    path('products/', views.products,name='products'),
    path('customers/', views.customers,name='customers'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('createorder/<str:pk>/',views.createOrder,name='createOrder'),
    path('updateorder/<str:pk>/',views.updateOrder,name="updateOrder"),
    path('deleteorder/<str:pk>/',views.deleteOrder,name="deleteOrder"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),

]
