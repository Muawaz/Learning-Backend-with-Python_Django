from rest_framework import serializers

class course_serializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    instructor = serializers.CharField(max_length=255)
    duration = serializers.CharField(max_length=255)