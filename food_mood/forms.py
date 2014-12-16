from food_mood.models import UserProfile, Entry
from django.contrib.auth.models import User
from django import forms
from django.forms import NumberInput

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'photo')
        
class AddForm(forms.ModelForm):
    mood = forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'min': 1, 'max': 10, 'onchange':'updateTextInput(this.value);'}))
    
    class Meta:
        model = Entry
        fields = ('meal', 'food', 'mood')
        