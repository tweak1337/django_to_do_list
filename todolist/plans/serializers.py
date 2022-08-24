from rest_framework.serializers import ModelSerializer

from plans.models import ActiveList


class ListSerializer(ModelSerializer):
    class Meta:
        model = ActiveList
        fields = ['deal', 'publish_date', 'is_done', 'done_date']
