from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError

state_choices = [
                 ('AL','Alabama'),
                 ('AK','Alaska'),
                 ('AZ','Arizona'),
                 ('AR','Arkansas'),
                 ('CA','California'),
                 ('CO','Colorado'),
                 ('CT','Connecticut'),
                 ('DE','Delaware'),
                 ('FL','Florida'),
                 ('GA','Georgia'),
                 ('HI','Hawaii'),
                 ('ID','Idaho'),
                 ('IL','Illinois'),
                 ('IN','Indiana'),
                 ('IA','Iowa'),
                 ('KS','Kansas'),
                 ('KY','Kentucky'),
                 ('LA','Louisiana'),
                 ('ME','Maine'),
                 ('MD','Maryland'),
                 ('MA','Massachusetts'),
                 ('MI','Michigan'),
                 ('MN','Minnesota'),
                 ('MS','Mississippi'),
                 ('MO','Missouri'),
                 ('MT','Montana'),
                 ('NE','Nebraska'),
                 ('NV','Nevada'),
                 ('NH','New Hampshire'),
                 ('NJ','New Jersey'),
                 ('NM','New Mexico'),
                 ('NY','New York'),
                 ('NC','North Carolina'),
                 ('ND','North Dakota'),
                 ('OH','Ohio'),
                 ('OK','Oklahoma'),
                 ('OR','Oregon'),
                 ('PA','Pennsylvania'),
                 ('RI','Rhode Island'),
                 ('SC','South Carolina'),
                 ('SD','South Dakota'),
                 ('TN','Tennessee'),
                 ('TX','Texas'),
                 ('UT','Utah'),
                 ('VT','Vermont'),
                 ('VA','Virginia'),
                 ('WA','Washington'),
                 ('WV','West Virginia'),
                 ('WI','Wisconsin'),
                 ('WY','Wyoming'),
]
    
def validate_usstate(value):
    usstates= [choice[0] for choice in state_choices]
    if value not in usstates:
        raise ValidationError(u'%s is not a valid US state' % value)

    
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, 
                             validators = [EmailValidator(message='Please input a valid email address')])#__call__ to enable instance() = instance.do()
    coin_balance = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    phone = models.CharField(max_length=20,null=True,blank=True,
                             validators=[RegexValidator('^((\(\d{3}\) |\d{3}-)\d{3}-\d{4})|(\d{10})$')])
    address_line_1 = models.CharField(max_length=50,null=True)
    address_line_2 = models.CharField(max_length=50,null=True,blank=True)
    postal_code = models.CharField(max_length=10,validators=[RegexValidator('^\d{5}(-\d{4})?$')])
    geo_lon = models.FloatField(null=True,blank=True)
    geo_lat = models.FloatField(null=True,blank=True)
    city_name = models.CharField(max_length=12)
    state_name = models.CharField(max_length=2, choices=state_choices)

    def __str__(self):
        return self.first_name + " " + self.last_name    
        
class Event(models.Model):
    event_type = models.IntegerField(default=0)
    event_title = models.CharField(max_length=50)
    event_description = models.TextField(null=True,blank=True)
    coin_amount = models.IntegerField(default=0)
    start_date = models.DateTimeField() #input_formats could be defined
    end_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    address_line_1 = models.CharField(max_length=50,null=True,blank=True)
    address_line_2 = models.CharField(max_length=50,null=True,blank=True)
    postal_code = models.CharField(max_length=10,null=True,blank=True,validators=[RegexValidator('^\d{5}(-\d{4})?$')])
    geo_lon = models.FloatField(null=True,blank=True)
    geo_lat = models.FloatField(null=True,blank=True)
    city_name = models.CharField(max_length=12)
    state_name = models.CharField(max_length=2, choices=state_choices)
    
    def __str__(self):
        return self.event_title[:20]
    
    
class Rating(models.Model):
    rating = models.IntegerField(default=4)# scale of 5
    comments = models.TextField(null=True,blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event)
    ratee = models.ForeignKey(Profile, related_name='ratee')
    rater = models.ForeignKey(Profile, related_name='rater')
    
    def __str__(self):
        return str(self.ratee) + "_" + str(self.event)
    
    
    

