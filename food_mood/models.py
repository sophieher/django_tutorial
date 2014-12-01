from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    meal = models.IntegerField(default=1)   #number of the meal, 1 for first, etc
    food = models.CharField(max_length=200) 
    mood = models.IntegerField(default=10)  #mood from 1 sucky to 10 the best
    pub_date = models.DateTimeField('date published')
    eater = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='entries')
    
    def __unicode__(self):
        return self.food
    
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    eater = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.eater.username