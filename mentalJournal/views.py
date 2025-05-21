from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import JournalEntry, Trigger, Suggestion
from .serializers import JournalEntrySerializer, TriggerSerializer, SuggestionSerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

class TriggerViewSet(viewsets.ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer
    permission_classes = [permissions.IsAuthenticated]

class SuggestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SuggestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        trigger_id = self.request.query_params.get('trigger')
        return Suggestion.objects.filter(trigger_id=trigger_id)
