from rest_framework import viewsets, generics, permissions
from .serializer import *
from rest_framework.viewsets import ViewSet
from .models import *


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryViewDelete(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryAllView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskStatus(generics.ListAPIView):
    def get_queryset(self, *args, **kwargs):
        q = Task.objects.filter(status=self.kwargs["pk"])
        return q

    serializer_class = TaskSerializer
