from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r"tasks_vs/router", TaskView)

urlpatterns = [
    path("", include(router.urls)),
    path("category/generics/<int:pk>/", CategoryView.as_view()),
    path("category/generics/all/", CategoryAllView.as_view()),
    path("category/view/delete/<int:pk>/", CategoryViewDelete.as_view()),
    path("category/status/<str:pk>/", TaskStatus.as_view())
]
