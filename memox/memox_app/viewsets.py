from rest_framework import viewsets
from .import models
from .import serializer

class MemoViewset(viewsets.ModelViewSet):
    queryset = models.Memo.objects.all()
    serializer_class = serializer.MemoSerializer