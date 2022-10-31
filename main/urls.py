from django.urls import path
from .views import list_view, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list', list_view, name='list'),
]