from django.urls import path

from ads.views import AdView, AdCreateView, AdListView

app_name = 'ads'

urlpatterns = [
    path('create/', AdCreateView.as_view()),
    path('', AdListView()),
    path('<int:pk>/', AdView.as_view())
]