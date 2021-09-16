from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    url(r'^query_storage$', views.query_storage, name='query_storage'),
    url(r'^query_history$', views.query_history, name='query_history'),

    url(r'^add_warehouse$', views.add_warehouse, name='add_warehouse'),
    url(r'^add_product$', views.add_product, name='add_product'),
    url(r'^add_customer$', views.add_customer, name='add_customer'),
    url(r'^add_supplier$', views.add_warehouse, name='add_supplier'),
    url(r'^add_technician$', views.add_warehouse, name='add_technician'),

    url(r'^add_stock$', views.add_warehouse, name='add_technician'),
    url(r'^add_service$', views.add_warehouse, name='add_technician'),
    url(r'^add_sale$', views.add_warehouse, name='add_technician'),

    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

