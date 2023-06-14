from django.shortcuts import render, redirect

from gamesPlayApp.web.forms import ProfileCreateForm, GameCreateForm, ProfileEditForm, ProfileDeleteForm, \
    GameDeleteForm, GameEditForm, ProfileDetailsForm
from gamesPlayApp.web.models import Profile, Game
from gamesPlayApp.web.utils import get_average_rating


def index(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    games = Game.objects.all()

    if games:
        avg_rating = get_average_rating(games)
    else:
        avg_rating = 0.0

    if request.method == 'GET':
        form = ProfileDetailsForm(instance=profile)
    else:
        form = ProfileDetailsForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
        'games_count': games.count(),
        'avg_rating': avg_rating,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()

            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)


def dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
        'profile': Profile.objects.get(),
    }

    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'profile': Profile.objects.get(),
    }

    return render(request, 'create-game.html', context)


def details_game(request, id):
    game = Game.objects \
        .filter(id=id) \
        .get()

    context = {
        'game': game,
        'profile': Profile.objects.get()
    }

    return render(request, 'details-game.html', context)


def edit_game(request, id):
    game = Game.objects \
        .filter(id=id) \
        .get()

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'game': game,
        'form': form,
        'profile': Profile.objects.get()
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, id):
    game = Game.objects \
        .filter(id=id) \
        .get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)

        if form.is_valid():
            game.delete()

            return redirect('dashboard')

    context = {
        'game': game,
        'form': form,
        'profile': Profile.objects.get()
    }

    return render(request, 'delete-game.html', context)
