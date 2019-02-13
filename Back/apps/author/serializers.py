from rest_framework import serializers
from .models import Author


class AuthorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'a_url', 'up_name', 'sex', 'register_time', 'following', 'follower', 'videos', 'album', 'views')
