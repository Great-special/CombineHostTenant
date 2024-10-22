from django.urls import path
from .views import index_account, user_register, login_user


urlpatterns = [
   path('', index_account, name="account_index"),
   path('register/', user_register, name="user_register"),
   path('login/', login_user, name='login'),
]

