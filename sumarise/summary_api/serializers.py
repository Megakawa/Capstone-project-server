from rest_framework import serializers

class SummaryTextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    percentage = serializers.IntegerField(required=True, min_value=1, max_value=100)

class SummaryLinkSerializer(serializers.Serializer):
    url = serializers.URLField()
    percentage = serializers.IntegerField(required=True, min_value=1, max_value=100)
