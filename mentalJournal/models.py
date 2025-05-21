from django.db import models
from django.contrib.auth.models import User

# These are my models
class Trigger(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(True)

class Suggestion(models.Model):
    trigger = models.ForeignKey(Trigger,on_delete=models.CASCADE)
    content = models.TextField()

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    mood = models.CharField(max_length=150)
    content = models.TextField()
    trigger = models.ForeignKey(Trigger,null=True, blank=Trigger, on_delete=models.CASCADE)        
