from django.db import models
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hash = models.CharField(max_length=32, default= None, null = True)
    txId = models.CharField(max_length=66, default=None, null = True)


    def write_on_chain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()



    def __str__(self):
        return self.title
