from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView, getUser

app_name = 'users'

urlpatterns = [
    path('register/',CustomUserCreate.as_view(), name="create_user"),
    path('logout/backlist/', BlacklistTokenView.as_view(),
         name='blacklist'),
    path('logedUser/',getUser.as_view(),name='LogedUser'),
]