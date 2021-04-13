from django.core.management.base import BaseCommand, CommandError
from tracker.models import SquirrelTracker
import csv
import os

class Command(BaseCommand):
    help = 'Export the data in CSV format'

    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **kwargs):
        with open(kwargs['path'],'w',) as csv_writer:
            parameters = [
                    'X',
                    'Y',
                    'Unique Squirrel ID',
                    'Shift',
                    'Date',
                    'Age',
                    'Primary Fur Color',
                    'Location',
                    'Specific Location',
                    'Running',
                    'Chasing',
                    'Climbing',
                    'Eating',
                    'Foraging',
                    'Other Activities',
                    'Kuks',
                    'Quaas',
                    'Moans',
                    'Tail flags',
                    'Tail twitches',
                    'Approaches',
                    'Indifferent',
                    'Runs from',
                    ]
            writer = csv.DictWriter(csv_writer,fieldnames=parameters)
            writer.writeheader()

            for squirrel in SquirrelTracker.objects.all():
                writer.writerow({
                    'X':squirrel.X,
                    'Y':squirrel.Y,
                    'Unique Squirrel ID': squirrel.Unique_Squirrel_ID,
                    'Shift': squirrel.Shift,
                    'Date': squirrel.Date,
                    'Age': squirrel.Age,
                    'Primary Fur Color': squirrel.Primary_Fur_Color,
                    'Location':squirrel.Location,
                    'Specific Location': squirrel.Specific_Location,
                    'Running': squirrel.Running,
                    'Chasing': squirrel.Chasing,
                    'Climbing': squirrel.Climbing,
                    'Eating': squirrel.Eating,
                    'Foraging': squirrel.Foraging,
                    'Other Activities': squirrel.Other_Activities,
                    'Kuks': squirrel.Kuks,
                    'Quaas': squirrel.Quaas,
                    'Moans': squirrel.Moans,
                    'Tail flags': squirrel.Tail_Flags,
                    'Tail twitches':squirrel.Tail_Twitches,
                    'Approaches': squirrel.Approaches,
                    'Indifferent': squirrel.Indifferent,
                    'Runs from': squirrel.Runs_From,
                    })
            self.stdout.write(self.style.SUCCESS('Successfully Create:{}'.format(kwargs['path'])))
