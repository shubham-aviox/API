from rest_framework import serializers
from .models import Album, Track
import time

class TrackListingField(serializers.RelatedField):
    def to_representation(self, value):
        duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return 'Track %d: %s (%s)' % (value.order, value.title, duration)

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackListingField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('tracks', 'name', 'artist', )
# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ('album','order', 'title', 'duration')

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ('name', 'artist', 'tracks')
    
#     print(tracks)