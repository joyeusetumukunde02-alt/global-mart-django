from django.urls import path
from.import views
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

urlpatterns = [
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('',views.avilableProduct_view, name='product'),
    path('order/',views.order_view, name='order'),
   
    path('employe/order_list/',views.order_list,name='order_list'),
    path("employe/", EmployeeListView.as_view(), name="employee_list"),
    path("employe/add/", EmployeeCreateView.as_view(), name="employee_create"),
    path("edit/<int:pk>/", EmployeeUpdateView.as_view(), name="employee_update"),
    path("delete/<int:pk>/", EmployeeDeleteView.as_view(), name="employee_delete"),
    path('overView/',views.overView,name='overView'),
    path('employe/dep/',views.dep,name='dep'), 
    path('add-comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    path('contact/',views.contact,name='contact'),
    # Category URLs
    path('products/phones/', views.phone_products, name='phones'),
    path('products/computers/', views.computer_products, name='computers'),
    path('products/accessories/', views.accessories_products, name='accessories'),
    path('products/phones/order',views.order_view, name='order'),
    path('products/computers/order',views.order_view, name='order'),
    path('products/accessories/order',views.order_view, name='order'),
   

    
]
