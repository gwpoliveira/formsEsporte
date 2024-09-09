# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inscritos/', views.lista_inscritos, name='lista_inscritos'),
    path('exportar-inscritos/', views.exportar_inscritos_excel, name='exportar_inscritos_excel'),
    path('inscricao/sucesso/', views.success_view, name='success'),
]
