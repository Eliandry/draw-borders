from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.MainView.as_view(),name='main'),
    path('level/<int:pk>/', views.LevelDetail.as_view()),
    path('level/<int:pk>/result/',views.result,name='result')
]