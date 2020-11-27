from django.shortcuts import render

from random import sample

from data import departures, description, subtitle, tours


def MainView(request):

    tours_list = sample(tours.items(), 6)

    context = {
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'tours': tours_list,
    }

    return render(request, 'index.html', context=context)


def DepartureView(request, departure):

    tour_list = {}

    for i in tours:
        if tours[i]['departure'] == departure:
            tour_list[i] = tours[i]

    tours_quantity = len(tour_list)

    nights = []
    price = []

    for n in tour_list:
        nights.append(tour_list[n]['nights'])
        price.append(tour_list[n]['price'])

    nights_min = min(nights)
    nights_max = max(nights)
    price_min = min(price)
    price_max = max(price)

    departure_url = departures[departure]
    context = {
        'departures': departures,
        'departure_url': departure_url,
        'tour_list': tour_list,
        'tours_quantity': tours_quantity,
        'nights_min': nights_min,
        'nights_max': nights_max,
        'price_min': price_min,
        'price_max': price_max,
    }

    return render(request, 'departure.html', context=context)


def TourView(request, id):

    depar = tours[id]['departure']
    dep = departures[depar]
    stars = int(tours[id]['stars']) * '★'
    context = {
        'tour': tours[id],
        'departure': dep,
        'stars': stars,
        'departures': departures,
    }

    return render(request, 'tour.html', context=context)
