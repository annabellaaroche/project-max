from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView

app_name = 'users'

urlpatterns = [
    path('register/',CustomUserCreate.as_view(), name="create_user"),
    path('logout/backlist/', BlacklistTokenView.as_view(),
         name='blacklist')
]