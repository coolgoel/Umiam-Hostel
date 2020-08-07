from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Gallery, GalleryOverview, Achievement, QuickLinks, HMC, Facility


def get_hmc(year):
    student_designations = [
        'General Secretary',
        'Welfare Secretary',
        'Mess Convener',
        'Cultural Secretary',
        'Literary Secretary',
        'Technical Secretary',
        'Sports Secretary',
        'Maintenance Secretary',
    ]
    other_designations = [
        'Warden',
        'Associate Warden',
        'Caretaker'
    ]

    d = dict()

    try:
        hmc = HMC.objects.get(year=year)
    except HMC.DoesNotExist:
        return d

    hmc = hmc.hmc_members.all()
    hmc_list = []
    warden_list = []
    for designation in other_designations:
        other_members = hmc.filter(designation=designation)
        for other_member in other_members:
            warden_list.append(other_member)
    for designation in student_designations:
        hmc_members = hmc.filter(designation=designation)
        for hmc_member in hmc_members:
            hmc_list.append(hmc_member)

    hmc_rows = []
    for i in range(0, len(hmc_list), 3):
        hmc_rows.append(hmc_list[i:i + 3])

    d['warden_list'] = warden_list
    d['hmc'] = hmc_rows
    return d


def hmc(request, year):
    d = {'year': year}
    d.update(get_hmc(year))
    return render(request, 'hmc.html', d)


def index(request):
    achievements = Achievement.objects.all()
    gallery = Gallery.objects.all()
    gallery_overview = GalleryOverview.objects.all()
    quick_links = QuickLinks.objects.all().order_by('name')
    facilities = Facility.objects.all()

    gallery_list = []
    for image in gallery:
        gallery_list.append(image)

    gallery = []
    for i in range(0, len(gallery_list), 4):
        gallery.append(gallery_list[i:i+4])

    d = {'achievements': achievements,
         'gallery': gallery,
         'quick_links': quick_links,
         'gallery_overview': gallery_overview,
         'facilities': facilities}

    d.update(get_hmc(2019))
    return render(request, 'umIndex.html', d)
