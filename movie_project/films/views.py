from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm


def film_create_view(request):
    form = FilmForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('film_list')
    return render(request, 'films/film_form.html', {'form': form})


def film_list_view(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})