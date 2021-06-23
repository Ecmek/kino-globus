from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page


from .models import Cinema, ShowTime
from .forms import CinemaForm, ShowTimeForm

paginator_pages = 10


# @cache_page(20)
def index(request):
    films = Cinema.objects.filter(on_screen=True).prefetch_related('show_time')
    paginator = Paginator(films, paginator_pages)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page})


# @cache_page(20)
def show_end(request):
    films = Cinema.objects.filter(on_screen=False).prefetch_related('show_time')
    paginator = Paginator(films, paginator_pages)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'show_end.html', {'page': page})


@login_required
def add_cinema(request):
    form = CinemaForm(request.POST or None)
    if form.is_valid():
        cinema = form.save(commit=False)
        cinema.save()
        return redirect('index')
    context = {
        'header': 'Добавить ленту',
        'form': form
    }
    return render(request, 'new_item.html', context)


@login_required
def edit_cinema(request, id_cinema):
    cinema = get_object_or_404(Cinema, id=id_cinema)
    form = CinemaForm(request.POST or None, instance=cinema)
    if form.is_valid():
        cinema = form.save(commit=False)
        cinema.save()
        return redirect('index')
    context = {
        'header': 'Редактирование ленты',
        'form': form
    }
    return render(request, 'new_item.html', context)


@login_required
def add_show_time(request):
    form = ShowTimeForm(request.POST or None)
    if form.is_valid():
        cinema = form.save(commit=False)
        cinema.save()
        return redirect('index')
    context = {
        'header': 'Добавить сеанс',
        'form': form
    }
    return render(request, 'new_item.html', context)


@login_required
def edit_session(request, id_cinema, id_session):
    session = get_object_or_404(ShowTime, id=id_session, cinema=id_cinema)
    form = ShowTimeForm(request.POST or None, instance=session)
    if form.is_valid():
        session = form.save(commit=False)
        session.save()
        return redirect('index')
    context = {
        'header': 'Редактирование сеанса',
        'form': form
    }
    return render(request, 'new_item.html', context)


@login_required
def confrim_delete_session(request, id_cinema, id_session):
    film = get_object_or_404(Cinema, id=id_cinema)
    session = get_object_or_404(ShowTime, id=id_session, cinema=id_cinema)
    return render(request, 'session.html', {'session': session, 'film': film})


@login_required
def delete_session(request, id_cinema, id_session):
    session = get_object_or_404(ShowTime, id=id_session, cinema=id_cinema)
    session.delete()
    return redirect('index')


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
