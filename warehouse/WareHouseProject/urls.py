from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.index, name='index'),
	path('Companies/', views.company_detail, name='Companies Detail'),
	path('Goods/', views.goods_detail, name='Goods Detail'),
	path('Customers/', views.customers_detail, name='Customers Detail'),
	path('Goods/<int:good_id>/', views.good_info, name='Good Info'),
	path('Companies/<int:company_id>/', views.company_info, name='Company Info'),
	path('Customers/<int:customer_id>/', views.customer_info, name='Customer Info'),
	path('Create_Company/', views.company_create, name='Create Company'),
	path('Create_Customer/', views.customer_create, name='Create Customer'),
	path('Create_Good/', views.good_create, name='Create Good'),
	path('Goods/<int:id>/delete/', views.delete_good, name='Remove Good'),
	path('Companies/<int:id>/delete/', views.delete_company, name='Remove Company'),
	path('Customers/<int:id>/delete/', views.delete_customer, name='Remove Customer'),
	
]