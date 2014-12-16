from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib
import os

class Entry(models.Model):
    meal = models.IntegerField(default=1)   #number of the meal, 1 for first, etc
    food = models.CharField(max_length=200) 
    mood = models.IntegerField(default=5)  #mood from 1 sucky to 10 the best
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    eater = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='entries')
    
    def __unicode__(self):
        return self.food
    
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='profile')

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    photo = models.ImageField(upload_to='/static/profile_images/', blank=True)

    # thanks to sarahhagstrom for this unicode output
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
    
    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
 
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
        # return "http://local.host:8000/static/" + self.photo.url
        
    class Meta:
        db_table = 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
          result = EmailAddress.objects.filter(email=self.user.email)
          if len(result):
              return result[0].verified
        return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])