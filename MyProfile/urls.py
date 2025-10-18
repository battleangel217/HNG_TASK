from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileViews.as_view(), name="my profile")
]