from django.db import models
from authentication.models import User
class Note(models.Model):
    short_note = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.short_note or 'No Title'
    
