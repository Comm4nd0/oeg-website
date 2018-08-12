import sys, os

sys.path.append('/home/marco/oeg/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'oeg.settings'

import django
django.setup()

import csv
from pedigree.models import Goat, Breeder

with open('/home/marco/oeg/media/goat_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # breeder = row["breeder"]
        # current_owner = row["current_owner"]
        reg_no = row["reg_no"]
        name = row["name"]
        dob = row["dob"]
        dod = row["dod"]
        sex = row["sex"]
        sire = row["sire"]
        dam = row["dam"]
        notes = row["notes"]
        image = row["image"]
        min_milk_yield = row["min_milk_yield"]
        max_milk_yield = row["max_milk_yield"]
        avg_milk_yield = row["avg_milk_yield"]
        height_to_withers = row["height_to_withers"]
        first_prize = row["first_prize"]
        second_prize = row["second_prize"]
        third_prize = row["third_prize"]

        goat = Goat()
        # breeder_obj = Breeder.objects.get(prefix=breeder)
        # goat.breeder = breeder_obj.id
        # goat.current_owner = current_owner
        goat.reg_no = reg_no
        goat.name = name
        goat.dob = dob
        goat.dod = dod
        goat.sex = sex
        goat.sire = sire
        goat.dam = dam
        goat.notes = notes
        goat.image = image
        goat.min_milk_yield = min_milk_yield
        goat.max_milk_yield = max_milk_yield
        goat.avg_milk_yield = avg_milk_yield
        goat.height_to_withers = height_to_withers
        goat.first_prize = first_prize
        goat.second_prize = second_prize
        goat.third_prize = third_prize

        goat.save()


# with open('/home/marco/projects/oeg/media/Prefixes.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         prefix = row['prefix']
#
#         breeder = Breeder()
#         breeder.prefix = prefix
#
#         breeder.save()
