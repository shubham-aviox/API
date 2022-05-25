from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=30)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return self.order, self.title

    def __str__(self):
        return self.title