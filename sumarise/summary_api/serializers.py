from rest_framework import serializers

class SummaryTextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    n_sen = serializers.IntegerField(required=True, min_value=1)

class SummaryLinkSerializer(serializers.Serializer):
    url = serializers.URLField()
    n_sen = serializers.IntegerField(required=True, min_value=1)
