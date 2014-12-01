from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from food_mood.forms import UserForm, UserProfileForm

def index(request):
    # Request the context of the request.
       # The context contains information such as the client's machine details, for example.
       context = RequestContext(request)

       # Construct a dictionary to pass to the template engine as its context.
       # Note the key boldmessage is the same as {{ boldmessage }} in the template!
       context_dict = {'passedmessage': "showing off template vars"}

       # Return a rendered response to send to the client.
       # We make use of the shortcut function to make our lives easier.
       # Note that the first parameter is the template we wish to use.
       return render_to_response('food_mood/index.html', context_dict, context)
    
def signup(request):
    context = RequestContext(request)
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.eater = user
            
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
                
            profile.save()
            
            registered = True
            
        else:
            print user_form.errors, profile_form.errors
            
    else: #not a http post
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render_to_response(
            'food_mood/signup.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context
            )
    