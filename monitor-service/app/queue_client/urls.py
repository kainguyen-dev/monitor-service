from django.urls import path
from queue_client import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('queue_connection/', views.QueueConnectionList.as_view()),
    path('queue_connection/<int:pk>/', views.QueueConnectionDetail.as_view())
]
