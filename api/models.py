from django.db import models
from django.conf import settings


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    Description = models.CharField(max_length=255, null=False , blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=100, null=True , blank=True)
    source = models.FileField(upload_to='songs/' ,null=True , blank=True)
    album = models.ImageField(upload_to ='album/',null=True, blank=True)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return "{} - {} - {} - {} - {}- {}- {}- {}".format(self.id, self.title, self.Description , self.created_at, self.updated_at, self.label ,self.link , self.source , self.album)
    
    def delete(self, using=None, keep_parents=False):
        self.src.storage.delete(self.src.name)
        self.album.storage.delete(self.album.name)
        super().delete()