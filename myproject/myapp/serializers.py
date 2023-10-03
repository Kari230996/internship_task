from rest_framework import serializers
from .models import Lesson, LessonView

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ('lesson', 'view_time_seconds', 'status')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('lesson_name', 'video_link', 'duration_seconds')
              