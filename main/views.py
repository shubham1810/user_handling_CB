from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from models import *
from forms import UserProfileForm, UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    # return HttpResponse("Hello!")
    return render(request, "index.html")


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save()

            profile.user = user
            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, "register.html", context_dict)


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
            else:
                return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login details!")
    else:
        return render(request, "login.html", {})


def some_data(request):
    if request.user.is_authenticated():
        return render(request, "some_data.html", {})
    else:
        return HttpResponse("You are not authorized in this page!!")


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/main/')

@login_required
def leaderboard(request):
    users = UserProfile.objects.all().order_by('-score')

    assign_code = request.GET.get('a_code') or None
    if not assign_name is None:
        assignment = Assignment.objects.filter(assignment_code=assign_code)
        submission = submission.objects.filter()
    else:
        pass
    data = []
    for user in users:
        data.append([user.user.username, user.score])

    context_dict = {
        'data': data
    }

    # return HttpResponse("A")
    return render(request, "leaderboard.html", context_dict)