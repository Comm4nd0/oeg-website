from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Goat, Breeder
import csv


@login_required(login_url="/members/signup")
def search(request):
    breeders = Breeder.objects
    return render(request, 'search.html', {'breeders': breeders})


def search_res(request):
    return results(request, reg_no=None)


def view_from_admin(request, reg_no):
    return results(request, reg_no)


@login_required(login_url="/members/signup")
def results(request, reg_no):
    if request.POST:
        reg_no = request.POST['search']

    # lvl 1
    try:
        lvl1 = Goat.objects.get(reg_no__exact=reg_no.upper())
    except:
        breeders = Breeder.objects
        error = "no goats found using: "
        return render(request, 'search.html', {'breeders': breeders,
                                               'error': error,
                                               'reg_no': reg_no})

    data = {}

    data['lvl1'] = lvl1

    try:
        lvl2_1 = Goat.objects.get(name=lvl1.dam)
        data['lvl2_1'] = lvl2_1

    except:
        data['lvl2_1'] = ''

    try:
        lvl2_2 = Goat.objects.get(name=lvl1.sire)
        data['lvl2_2'] = lvl2_2


    except:
        data['lvl2_2'] = ''

    # lvl 3
    # 1
    try:
        lvl3_1 = Goat.objects.get(name=lvl2_1.dam)
        data['lvl3_1'] = lvl3_1

    except:
        data['lvl3_1'] = ''

    # 2
    try:
        lvl3_2 = Goat.objects.get(name=lvl2_1.sire)
        data['lvl3_2'] = lvl3_2

    except:
        data['lvl3_2'] = ''

    # 3
    try:
        lvl3_3 = Goat.objects.get(name=lvl2_2.dam)
        data['lvl3_3'] = lvl3_3

    except:
        data['lvl3_3'] = ''

    # 4
    try:
        lvl3_4 = Goat.objects.get(name=lvl2_2.sire)
        data['lvl3_4'] = lvl3_4

    except:
        data['lvl3_4'] = ''

    return render(request, 'results.html', data)


@login_required(login_url="/members/signup")
def breeder(request, breeder):
    breeder_details = Breeder.objects.get(prefix=breeder)
    pedigrees = Goat.objects.filter(breeder__prefix__exact=breeder)
    owned = Goat.objects.filter(current_owner__prefix__exact=breeder)
    return render(request, 'breeder.html', {'breeder_details': breeder_details,
                                            'pedigrees': pedigrees,
                                            'owned': owned})


@login_required(login_url="/members/signup")
def goat_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedigree_db.csv"'

    writer = csv.writer(response)
    writer.writerow(['breeder',
                     'current_owner',
                     'reg_no',
                     'name',
                     'dob',
                     'dod',
                     'sex',
                     'sire',
                     'dam',
                     'notes',
                     'image',
                     'min_milk_yield',
                     'max_milk_yield',
                     'avg_milk_yield',
                     'height_to_withers',
                     'first_prize',
                     'second_prize',
                     'third_prize'])
    goat = Goat.objects
    for row in goat.all():
        writer.writerow([row.breeder,
                         row.current_owner,
                         row.reg_no,
                         row.name,
                         row.dob,
                         row.dod,
                         row.sex,
                         row.sire,
                         row.dam,
                         row.notes,
                         row.image,
                         row.min_milk_yield,
                         row.max_milk_yield,
                         row.avg_milk_yield,
                         row.height_to_withers,
                         row.first_prize,
                         row.second_prize,
                         row.third_prize])

    return response


def breeder_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="breeder_db.csv"'

    writer = csv.writer(response)
    writer.writerow(['prefix',
                     'contact_name',
                     'address',
                     'phone_number1',
                     'phone_number2',
                     'email',
                     'active'])
    breeder = Breeder.objects
    for row in breeder.all():
        writer.writerow([row.prefix,
                         row.contact_name,
                         row.address,
                         row.phone_number1,
                         row.phone_number2,
                         row.email,
                         row.active
                         ])

    return response
