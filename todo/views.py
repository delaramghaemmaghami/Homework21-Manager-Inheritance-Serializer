from rest_framework import viewsets, generics, permissions
from .serializer import *
from rest_framework.viewsets import ViewSet
from .models import *


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]



class CategoryViewDelete(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryAllView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskStatus(generics.ListAPIView):
    def get_queryset(self, *args, **kwargs):
        q = Task.objects.filter(status=self.kwargs["status"])
        return q

    serializer_class = TaskSerializer
