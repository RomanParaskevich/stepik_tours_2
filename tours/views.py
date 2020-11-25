from django.shortcuts import render

from data import tours, departures, description, subtitle

def MainView(request):

    context = {
        'subtitle': subtitle,
        'description': description,
    }

    return render(request, 'index.html', context=context)


def DepartureView(request, departure):

    return render(request, 'departure.html')


def TourView(request, id):

    depar = tours[id]['departure']
    dep = departures[depar]
    stars = int(tours[id]['stars']) * '★'
    context = {
        'tour': tours[id],
        'departure': dep,
        'stars': stars,
    }

    return render(request, 'tour.html', context=context)
