from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout
from text2emotion import get_emotion
from .models import Submission, Therapy, Doctor, Game, Story
# Create your views here.

def generate_emotion_from_60_40_ratio(dCardModedl:str, PredictionModel:str) -> dict:
    return get_emotion(PredictionModel)

def satisfies_range(range_model, submission_model):
    for label, satis_range in range_model.range.items():
        if(not(getattr(submission_model, label) >= satis_range[0] and getattr(submission_model, label) <= satis_range[1])):
            return False
    return True
def home(request):

    '''
    Check if the user is authenticated, 
        - If Authenticated then we pass the username data to display at navbar
        - Else we return with normal login/register button
    '''

    user = request.user
    print(user)
    if(user.is_authenticated):
        return render(request, 'home.html', context={'username': user.username})


    return render(request, 'home.html')

def doctors(request):

    user = request.user
    doctors = list(Doctor.objects.all())
    if(user.is_authenticated):


        return render(request, 'doctors.html', context={'username': user.username, 'doctors': doctors})

    return render(request, 'doctors.html', context={'doctors': doctors})

def therapy(request):

    user = request.user
    filtered_tharapies = list(Therapy.objects.all())
    print("DBG:", filtered_tharapies)
    therapies = {
        'speech': [],
        'music': [],
        'song': []
    }

    for j in filtered_tharapies:
        therapies[j.group].append(j)
    if(user.is_authenticated):
        return render(request, 'therapy.html', context={'username': user.username, **therapies})

    return render(request, 'therapy.html', context=therapies)

def peronalized_therapy(request, *args, **kwargs):
    submission_id = kwargs.get('sid')

    try:

        submission = Submission.objects.get(pk=submission_id)

        filtered_tharapies = [ t for t in list(Therapy.objects.all()) if satisfies_range(t, submission) ]
        print("DBG:", filtered_tharapies)
        therapies = {
            'speech': [],
            'music': [],
            'song': []
        }

        for j in filtered_tharapies:
            therapies[j.group].append(j)
                

        return render(request, 'therapy.html', {'speech': therapies['speech'], 'music': therapies['music'], 'song': therapies['song'], 'username': request.user.username})

    except Submission.DoesNotExist as notFound:
        return redirect('Therapy | Neuron')

def peronalized_games(request, *args, **kwargs):
    submission_id = kwargs.get('sid')

    try:

        submission = Submission.objects.get(pk=submission_id)

        filtered_games= [ t for t in list(Game.objects.all()) if satisfies_range(t, submission) ]

        return render(request, 'game.html', {'games': filtered_games, 'username': request.user.username})

    except Submission.DoesNotExist as notFound:
        return redirect('Games | Neuron')

def personalized_stories(request, *args, **kwargs):
    submission_id = kwargs.get('sid')

    try:

        submission = Submission.objects.get(pk=submission_id)

        filtered_stories= [ t for t in list(Story.objects.all()) if satisfies_range(t, submission) ]

        return render(request, 'stories.html', {'stories': filtered_stories, 'username': request.user.username})

    except Submission.DoesNotExist as notFound:
        return redirect('stories | Neuron')



def peronalized_stories(request, *args, **kwargs):
    submission_id = kwargs.get('sid')

    try:

        submission = Submission.objects.get(pk=submission_id)

        filtered_stories= [ t for t in list(Story.objects.all()) if satisfies_range(t, submission) ]

        return render(request, 'stories.html', {'stories': filtered_stories, 'username': request.user.username})

    except Submission.DoesNotExist as notFound:
        return redirect('stories | Neuron')

def game(request):

    user = request.user
    if(user.is_authenticated):
        return render(request, 'game.html', context={'games': list(Game.objects.all()),'username': user.username})
    
    return render(request, 'game.html', context={'games': list(Game.objects.all())})

def doctors_by_city(request, *args, **kwargs):

    city = kwargs.get('city')

    doctors = [doctor for doctor in list(Doctor.objects.filter(location=city))]

    return render(request, 'doctors.html', context={'username': request.user.username if request.user.is_authenticated else None, 'doctors': doctors})

def stories(request):

    user = request.user
    if(user.is_authenticated):
        return render(request, 'stories.html', context={'stories': list(Story.objects.all()),'username': user.username})

    return render(request, 'stories.html', context={'stories': list(Story.objects.all())})


def blogs(request):

    user = request.user
    if(user.is_authenticated):
        return render(request, 'blogs.html', context={'username': user.username})

    return render(request, 'blogs.html')

def analytics(request):
    if(not request.user.is_authenticated):
        return redirect('SignUp | Neuron')
    # Compute submissions
    submissions = list(Submission.objects.filter(target_user=request.user))
    s = {
        '😃': {
            'color': 'green',
            'logs': []
        },
        '😨': {
            'color': 'yellow',
            'logs': []
        },
        '😢': {
            'color': 'red',
            'logs': []
        },
        '😯': {
            'color': 'blue',
            'logs': []
        },
        '😠': {
            'color': 'orange',
            'logs': []
        },
    }

    for submission in reversed(submissions):
        s['😃']['logs'].append(submission.happy)
        s['😢']['logs'].append(submission.sad)
        s['😯']['logs'].append(submission.surprise)
        s['😨']['logs'].append(submission.fear)
        s['😠']['logs'].append(submission.angry)

    return render(request, 'analytics.html', context={'submissions': submissions, 's_data': s, 'recent_sid': submissions[0].pk if len(submissions) > 0 else '', 'username': request.user.username, 'is_critical': request.user.username.lower()=='temp'})

def quiz(request):

    user = request.user
    if(request.method == 'POST'):
        emoji = request.POST.get('emoji') # Matters 60%
        feeling_descr = request.POST.get('feeling_descr') # Matters 40%
        print('-'*67)
        print(emoji, feeling_descr)
        op = generate_emotion_from_60_40_ratio(emoji, feeling_descr)
        # print("Hereis",op)
        my_submission = Submission.objects.create(target_user=user, angry=op['Angry'], sad=op['Sad'], surprise=op['Surprise'], happy=op['Happy'], fear=op['Fear'])

        return redirect('analytics')


    if(user.is_authenticated):
        return render(request, 'quiz.html', context={'username': user.username})

    return redirect('SignUp | Neuron')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User.objects.filter(username=username)
        if(not new_user.exists()):
            return render(request, 'home.html', context={'message': 'No such username found in record!'})

        new_user = new_user.first()
        correct_password = new_user.check_password(password)

        if(not correct_password):
            return render(request, 'home.html', context={'message': 'Incorrect Password'})


        auth_login(request, new_user)
        return redirect('Home Page | Neuron')

        # return render(request, 'home.html', context={'message': 'Account created, Logged in automatically!!'})
    else:
        return redirect('Home Page | Neuron')



def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if(not username or not email or not password):
            print("Falling")
            
            return render(request, 'signup.html', context={'message': 'Please provide valid username, email, password'})

        if(len(password) < 10):
            return render(request, 'signup.html', context={'message': 'Password must be at least 10 characters'})


        new_user, created = User.objects.get_or_create(username=username, defaults={'email':email})
        if(not created):
            # Username/Email already exists in DB
            return render(request, 'signup.html', context={'message': 'Username already exists!'})

        new_user.set_password(password)
        new_user.save()

        auth_login(request, new_user)
        return redirect('Home Page | Neuron')
        # return render(request, 'home.html', context={'message': 'Account created, Logged in automatically!!'})

@login_required  
def logout_user(request):

    logout(request)

    return redirect('Home Page | Neuron')
