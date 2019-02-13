from rest_framework import serializers
from .models import Video


class VideoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'url', 'title', 'types', 'public_time', 'author_name', 'author_url', 'author_id', 'view',
                  'danmaku', 'reply', 'favorite', 'coin', 'share', 'like')
