# Created by Joshua de Guzman on 05/07/2018
# @email code@jmdg.io

from rest_framework import serializers
from .. import models


class FeedTypeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = models.FeedType


class FeedSerializers(serializers.ModelSerializer):
    type = FeedTypeSerializers(source='type_id', many=False, read_only=True)

    class Meta:
        fields = ('id', 'type', 'type_id', 'cover_image', 'title', 'content', 'is_deleted', 'created_on', 'updated_at')
        model = models.Feed
