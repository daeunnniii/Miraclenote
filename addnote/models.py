from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    sttText = models.TextField()
    note_description = models.TextField()
    reg_date = models.DateTimeField()
    audio = models.ImageField(upload_to="audio")
    vis_js_nodes = models.TextField()
    vis_js_edges = models.TextField()

class NoteCnt(models.Model):
    save_cnt = models.IntegerField(default=0)
    input_date = models.IntegerField(default=0)

