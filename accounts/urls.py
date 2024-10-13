from django.urls import path
from .views import index_account


urlpatterns = [
   path('', index_account, name="account_index"),
   path('index/', index_account, name="test_index"),
]

