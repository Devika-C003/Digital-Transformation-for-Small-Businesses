from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Host(models.Model):
    class Meta:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'

    HostName = models.CharField(max_length=30)
    PhoneNumber = models.IntegerField()
    Email =  models.CharField(max_length=30)
    PropertyName = models.CharField(max_length=30)
    Location = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    Numberofrooms = models.IntegerField()
    Numberofguest = models.IntegerField()
    Priceofroom = models.IntegerField()
    # HostownershipDocuments = models.ImageField()
   
    def __str__(Host):
        return Host.PropertyName

class Booking(models.Model):
    Location = models.CharField(max_length=30)
    Checkindate = models.CharField(max_length=60)
    Checkoutdate = models.CharField(max_length=30)
    Rooms = models.IntegerField()
    Guest = models.IntegerField()
    
    def __str__(Host):
        return Host.Booking

class Accomodation(models.Models):

    
class ContactUs(models.Model):
	name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	email = models.CharField(max_length=15)
	writemessage = models.TextField(max_length=30)
    

	
	Propertyrooms = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(6)])
	Prpertylistingname = models.ForeignKey(Guest, on_delete=models.CASCADE)
class Bookings(models.Model):
	
	startDate = models.DateField()
	endDate = models.DateField()
	numGuests = models.IntegerField()
	Property = models.ForeignKey(PropertyListings, on_delete=models.CASCADE) #PROP ID FK
	GuestUser = models.ForeignKey(Guest, on_delete=models.CASCADE) #USER ID FK

	class Meta:
		constraints = [
			UniqueConstraint(fields=['startDate', 'Property'], name='unique_booking')
		]



class Images(models.Model):
	imgUrl = models.CharField(max_length=100)
	Property = models.ForeignKey(PropertyListings, on_delete=models.CASCADE) #PROP ID FK
	image = models.ImageField()

class Amenities(models.Model):
    place = models.OneToOneField(
        PropertyListings,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    wifi = models.BooleanField(default=False)
    Ratings=models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    AC= models.BooleanField(default=False)
    Washingmachine= models.BooleanField(default=False)


	
##Create your models here.

    def __str__(self):
        return self.name
    
    def formatted_date(self):
        return self.event_date.strftime('%d-%m-%Y')

    def formatted_start_time(self):
        return self.start_time.strftime('%H:%M')

    def formatted_end_time(self):
        return self.end_time.strftime('%H:%M')



    Registrtion  = models.ForeignKey(
    Registration, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField( null=False, blank=False)
    phone_ = Registrationphoneno= models.CharFieldRegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[Registrationphoneno= models.CharField], max_length=17, blank=True) # Validators should be a list

    def __str__(self):
        return self.name
