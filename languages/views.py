from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import (Paradigm, Language, Programmer)
from .serializers import (ParadigmSerializer,
                         LanguageSerializer,
                         ProgrammerSerializer)
 

class ParadigmViewSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
    

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
