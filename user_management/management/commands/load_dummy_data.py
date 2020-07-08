import json
from copy import deepcopy
from django.core.management.base import BaseCommand
from user_management.models import *

#This is the sample data to be imported to db
user_data = [
    { 
        "user_id": "W012A3CDE",
        "real_name": "Egon Spengler",
        "tz": "America/Los_Angeles",
        "period":[
                 {
					"start_time": "2020-02-01 13:33:00.241528+05:30",
					"end_time": "2020-02-01 13:54:00.241528+05:30"
				},
				{
					"start_time": "2020-03-01 11:11:00.241528+05:30",
					"end_time": "2020-03-01 14:00:00.241528+05:30",
				},
				{
					"start_time": "2020-03-16 05:33:00.241528+05:30",
					"end_time":"2020-03-16 08:02:00.241528+05:30"
				}
        ]
    },
    { 
        "user_id": "W07QCRPA4",
        "real_name": "Glinda Southgood",
        "tz": "Asia/Kolkata" ,
        "period":[
                {
					"start_time": "2020-02-01 13:33:00.241528+05:30",
					"end_time": "2020-02-01 13:54:00.241528+05:30"
				},
				{
					"start_time": "2020-03-01 11:11:00.241528+05:30",
					"end_time": "2020-03-01 14:00:00.241528+05:30",
				},
				{
					"start_time": "2020-03-16 05:33:00.241528+05:30",
					"end_time":"2020-03-16 08:02:00.241528+05:30"
				}
        ]
    }
]

#Command to import sample data from the dict to database
class Command(BaseCommand):
    help = 'For loading initial data'

    def handle(self, *args, **kwargs):
        # delete all records in the table and re-create it
        UserData.objects.all().delete()
        ActivityPeriod.objects.all().delete()
        for item in user_data:
            created_user = UserData.objects.create(user_id=item['user_id'],real_name = item['real_name'],tz=item['tz'])
            for period in item["period"]:
                ActivityPeriod.objects.create(user=created_user, start_time=period['start_time'], end_time=period['end_time'] )

