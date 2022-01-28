
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from Todo.views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', PlanListAPIView.as_view()),
    path('todo/<int:pk>/', RetriveAPIGetView.as_view()),
    # path('get-token/', obtain_auth_token),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    # path('todoa/dd/', PlanCreateAPIView.as_view()),
]


