from django.urls import path
from . import views

urlpatterns = [
    path('', views.deck_list, name='deck_list'),
    path('deck/<int:pk>/', views.deck_detail, name='deck_detail'),
    path('deck/new/', views.deck_create, name='deck_create'),
    path('deck/<int:pk>/edit/', views.deck_update, name='deck_update'),
    path('deck/<int:pk>/delete/', views.deck_delete, name='deck_delete'),
    path('deck/<int:deck_id>/card/new/', views.card_create, name='card_create'),
    path('card/<int:pk>/edit/', views.card_update, name='card_update'),
    path('card/<int:pk>/delete/', views.card_delete, name='card_delete'),
    path('deck/<int:deck_id>/study/', views.study, name='study'),
]