from django.core.management.base import BaseCommand, CommandError
from tracker.models import SquirrelTracker
import csv
import os
import datetime

class Command(BaseCommand):
    help = 'Import squirrel data from csv file'

    def add_arguments(self,parser):
        parser.add_argument('path',nargs='+', type = str)
        
    def handle(self, *args, **options):

        def convert_boo(text):
            if text.lower() == 'true':
                return True
            elif text.lower()=='false':
                return False
            else:
                return None

        for path in options['path']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(path)))
            with open(path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = list(csv_reader)
                for row in data:
                    ST = SquirrelTracker()
                    ST.X = row['X']
                    ST.Y = row['Y']
                    ST.Unique_Squirrel_ID = row['Unique Squirrel ID']
                    ST.Shift = row['Shift']
                    ST.Date = datetime.datetime.strptime(row['Date'],'%m%d%Y')
                    ST.Age = row['Age']
                    ST.Primary_Fur_Color = row['Primary Fur Color']
                    ST.Location = row['Location']
                    ST.Specific_Location = row['Specific Location']
                    ST.Running = convert_boo(row['Running'])
                    ST.Chasing = convert_boo(row['Chasing'])
                    ST.Climbing = convert_boo(row['Climbing'])
                    ST.Eating = convert_boo(row['Eating'])
                    ST.Foraging = convert_boo(row['Foraging'])
                    ST.Other_Activities = row['Other Activities']
                    ST.Kuks = convert_boo(row['Kuks'])
                    ST.Quaas = convert_boo(row['Quaas'])
                    ST.Moans = convert_boo(row['Moans'])
                    ST.Tail_Flags = convert_boo(row['Tail flags'])
                    ST.Tail_Twitches = convert_boo(row['Tail twitches'])
                    ST.Approaches = convert_boo(row['Approaches'])
                    ST.Indifferent = convert_boo(row['Indifferent'])
                    ST.Runs_From =convert_boo(row['Runs from'])
                    ST.save()
