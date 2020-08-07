from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, ValidationError, RegexValidator
# Create your models here.


def is_iitg_email(value):
    domain = value.split('@')[1]
    if domain == 'iitg.ac.in':
        return value
    else:
        raise ValidationError('Enter a Valid IITG Email Address')


class Facility(models.Model):
    facility_name = models.CharField(max_length=64)
    details = models.CharField(blank=True, max_length=1024)
    pic = models.ImageField()

    def __str__(self):
        return self.facility_name


class HMC(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return "HMC {}".format(self.year)


class HMCMember(models.Model):
    hmc = models.ForeignKey(HMC, on_delete=models.CASCADE, related_name='hmc_members')
    GENSEC = 'General Secretary'
    WELFY = 'Welfare Secretary'
    MESSI = 'Mess Convener'
    CULTY = 'Cultural Secretary'
    LITTY = 'Literary Secretary'
    TECHY = 'Technical Secretary'
    SPORTY = 'Sports Secretary'
    MENTY = 'Maintenance Secretary'
    WARDEN = 'Warden'
    ASS_WARDEN = 'Associate Warden'
    CARETAKER = 'Caretaker'

    DESIGNATION_CHOICES = (
        (GENSEC, GENSEC),
        (WELFY, WELFY),
        (MESSI, MESSI),
        (CULTY, CULTY),
        (LITTY, LITTY),
        (TECHY, TECHY),
        (SPORTY, SPORTY),
        (MENTY, MENTY),
        (WARDEN, WARDEN),
        (ASS_WARDEN, ASS_WARDEN),
        (CARETAKER, CARETAKER)
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hmc_member')
    profile_pic = models.ImageField()
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    iitg_email_validator = EmailValidator(whitelist=['iitg.ac.in'])
    iitg_email = models.EmailField(validators=[is_iitg_email])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Achievement(models.Model):
    achievement_name = models.CharField(max_length=256)
    achievement_description = models.CharField(max_length=1024, blank=True)
    achievement_pic = models.ImageField()

    def __str__(self):
        return self.achievement_name


class GalleryOverview(models.Model):
    event_name = models.CharField(max_length=256)
    event_description = models.CharField(max_length=1024, blank=True)
    event_pic = models.ImageField()

    def __str__(self):
        return self.event_name


class Gallery(models.Model):
    event_name = models.CharField(max_length=256)
    event_description = models.CharField(max_length=1024, blank=True)
    event_pic = models.ImageField()

    def __str__(self):
        return self.event_name


class QuickLinks(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField()

    def __str__(self):
        return self.name