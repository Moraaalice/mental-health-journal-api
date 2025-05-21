from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JournalEntryViewSet, TriggerViewSet, SuggestionViewSet

router = DefaultRouter()
router.register('journal', JournalEntryViewSet, basename='journal')
router.register('triggers', TriggerViewSet, basename='trigger')
router.register('suggestions', SuggestionViewSet, basename='suggestion')



urlpatterns = [
    
]