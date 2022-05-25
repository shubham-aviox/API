from django.http import JsonResponse
from django.shortcuts import render
from .models import Country, State, City
from django.db.models import Lookup


# Create your views here.
def home(request):
    # country1 = Country.objects.filter(id__range=(1, 3))
    country1 = Country.objects.filter(name__contains='u')
    print(country1)
    country = Country.objects.all()
    state = State.objects.all()
    city = City.objects.all()
    return render(request, 'home.html', {'countries': country, 'states': state, 'cities': city})


def get_states_ajax(request):
    if request.method == 'GET':
        print(request.GET)
        country_id = request.GET.get('country_id')
        country = Country.objects.get(id=country_id)
        state = State.objects.filter(country=country)
        result = list(state.values('id', 'name'))
        # print(result)
    return JsonResponse(result,  safe = False)


def get_cities_ajax(request):
    if request.method == 'GET':
        state_id = request.GET.get('state_id')
        print(state_id)
        state = State.objects.get(id=state_id)
        print(state,'pppppppppppppppp')
        city = City.objects.filter(state=state)
        print('cccccccccc',city)
        result1 = list(city.values('id', 'name'))
        print(result1)
    return JsonResponse(result1,  safe = False)


class NotEqual(Lookup):
    lookup = 'ne'

    def as_sql(self, compiler, connection):
        pass