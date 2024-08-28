from django.urls import path
from .views import AsyncExampleView

urlpatterns = [
    path('async-view/', AsyncExampleView.as_view(), name='async_example'),
]