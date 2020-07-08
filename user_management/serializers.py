from rest_framework import serializers
from .models import *


#This the Activty Period Serializer used as nested inside UserDataSerializer
class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%B %d %Y  %H:%M %p", required=False, read_only=True)
    end_time = serializers.DateTimeField(format="%B %d %Y  %H:%M %p", required=False, read_only=True)

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

#This the User Serializer for getting user details 
class UserDataSerializer(serializers.ModelSerializer):
    activity_periods = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    class Meta:
        model = UserData
        fields = ('id', 'real_name', 'tz','activity_periods')

    def get_id(self, data):
        return data.user_id

    def get_activity_periods(self, data):
        try:
            period = ActivityPeriod.objects.filter(user_id=data.id)
            return  ActivityPeriodSerializer(period, many=True).data
        except:
            return ""
