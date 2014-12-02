from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from food_mood.forms import UserForm, UserProfileForm
from food_mood.models import Entry

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

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
            
def signin(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/food_mood/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your FoodMood account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('food_mood/login.html', {}, context)
        
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/food_mood/')
  
def entries(request):  
    url = 'food_mood/entries.html'
    foodmood_list = Entry.objects.order_by('-pub_date')
    context = {'foodmood_list':foodmood_list}
    return render(request, url, context)
    
def entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'food_mood/entry.html', {'entry': entry})
    