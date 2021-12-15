from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r"api/router/AllTasks", TaskView)

urlpatterns = [
    path("task/", include(router.urls)),
    path("category/<int:pk>/", CategoryView.as_view()),
    path("category/all/", CategoryAllView.as_view()),
    path("category/delete/<int:pk>/", CategoryDeleteView.as_view()),
    path("category/<str:status>/", TaskStatus.as_view())
]
