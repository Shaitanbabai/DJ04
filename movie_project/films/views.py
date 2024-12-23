import logging
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Создайте логгер для вашего приложения
logger = logging.getLogger('myapp')  # замените 'myapp' на имя вашего приложения


def film_create_view(request):
    logger.debug("Entering film_create_view")
    form = FilmForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info("Film created successfully")
        return redirect('film_list')
    logger.debug("Rendering film_form.html with form errors")
    return render(request, 'films/film_form.html', {'form': form})


def film_list_view(request):
    logger.debug("Entering film_list_view")
    films = Film.objects.all()
    logger.info(f"Retrieved {len(films)} films from database")
    return render(request, 'films/film_list.html', {'films': films})