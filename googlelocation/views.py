from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import LocationForm
from .models import SourceLocation, SuperMarket,PublicServices,Competitor,Apartments,Retails,Restaurants
import json
from django import views
import googlemaps

def home(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            radiuss = form.cleaned_data['radius']
            latitude,longitude = map(float,location.split(','))
            Google_API_KEY = 'AIzaSyCNJ0iv-Why9tmFmkTZrIVPp_B_qMZYQpg'
            SourceLocation.objects.all().delete()
            SuperMarket.objects.all().delete()
            PublicServices.objects.all().delete()
            Competitor.objects.all().delete()
            Apartments.objects.all().delete()
            Retails.objects.all().delete()
            Restaurants.objects.all().delete()
            
            gmaps = googlemaps.Client(key=Google_API_KEY)

            # source database
            source_location = SourceLocation.objects.create(
                Source_lat = latitude,
                Source_lon = longitude)
            # competitors database
            competitor = ['KFC','Burger King',"McDonald's",'Pizza Hut',"Domino's"]
            nearby_competitors = []
            for comp in competitor:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = comp)
            
                if places_result['status'] == 'OK':
                    nearby_competitors.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_competitors:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                if result['status']=='OK':
                    element = result['rows'][0]['elements'][0]
                    if element['status'] == 'OK':
                        distance = element['distance']['text']
                        duration = element['duration']['text']
                    else:
                        distance = "cann't find"
                        duration = "cann't find"
                Competitor.objects.create(
                    name = place.get('name','No Name'),
                    status = place.get('business_status','default'),
                    address = place.get('vicinity','unknown'),
                    coordinates = coordinate,
                    types = place.get('types',[]),
                    rating = place.get('rating',0),
                    user_rating = place.get('user_ratings_total',0),
                    Travel_Distance = distance,
                    Travel_Time = duration,
                    source_location = source_location
                )
            

            # supermarket database
            nearby_supermarket = []    
            supermarket = ['Mall','Supermarket','Vishal Mega mart','Croma','D-mart','Trends','smart bazaar','Reliance Digital']
            for market in supermarket:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = market)
                if places_result['status'] == 'OK':
                    nearby_supermarket.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_supermarket:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 100) and (place.get('rating',0)>3):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    SuperMarket.objects.create(
                        name = place.get('name','No Name'),
                        status = place.get('business_status','default'),
                        address = place.get('vicinity','unknown'),
                        coordinates = coordinate,
                        types = place.get('types',[]),
                        rating = place.get('rating',0),
                        user_rating = place.get('user_ratings_total',0),
                        Travel_Distance = distance,
                        Travel_Time = duration,
                        source_location = source_location
                    )
                else:
                    result['status'] == 'Error'
                
            # PublicServices database 
            nearby_publicservices = []  
            publicservices = ['Bus Stand','School','college','University','Tourist']  
            
            for public in publicservices:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = public)
                if places_result['status'] == 'OK':
                    nearby_publicservices.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_publicservices:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 100) and (place.get('rating',0)>3):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    PublicServices.objects.create(
                        name = place.get('name','No Name'),
                        status = place.get('business_status','default'),
                        address = place.get('vicinity','unknown'),
                        coordinates = coordinate,
                        types = place.get('types',[]),
                        rating = place.get('rating',0),
                        user_rating = place.get('user_ratings_total',0),
                        Travel_Distance = distance,
                        Travel_Time = duration,
                        source_location = source_location
                    )
                else:
                    result['status'] == 'Error'
                
            #Apartments database

            nearby_apartments = [] 
            apartments = ['Appartments'] 
              
            
            for apartment in apartments:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = apartment)
                if places_result['status'] == 'OK':
                    nearby_apartments.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_apartments:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 100) and (place.get('rating',0)>3):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    Apartments.objects.create(
                        name = place.get('name','No Name'),
                        status = place.get('business_status','default'),
                        address = place.get('vicinity','unknown'),
                        coordinates = coordinate,
                        types = place.get('types',[]),
                        rating = place.get('rating',0),
                        user_rating = place.get('user_ratings_total',0),
                        Travel_Distance = distance,
                        Travel_Time = duration,
                        source_location = source_location
                    )
                else:
                    result['status'] == 'Error'
                
            # retails database
            nearby_retails = [] 
            retails = ['retail shop'] 
              
            
            for retail in retails:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = retail)
                if places_result['status'] == 'OK':
                    nearby_retails.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_retails:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 100) and (place.get('rating',0)>3):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    Retails.objects.create(
                        name = place.get('name','No Name'),
                        status = place.get('business_status','default'),
                        address = place.get('vicinity','unknown'),
                        coordinates = coordinate,
                        types = place.get('types',[]),
                        rating = place.get('rating',0),
                        user_rating = place.get('user_ratings_total',0),
                        Travel_Distance = distance,
                        Travel_Time = duration,
                        source_location = source_location
                    )
                else:
                    result['status'] == 'Error'
                
            # restaurants Database

            exclude_competitor = {'KFC','Burger King',"McDonald's",'Pizza Hut',"Domino's"}
            nearby_restaurant = []
            restaurants = ['Restaurant']
            for restaurant in restaurants:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = restaurant)
                if places_result['status'] == 'OK':
                    nearby_restaurant.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_restaurant:
                if place['name'] not in exclude_competitor and (place.get('user_ratings_total',0) > 100) and (place.get('rating',0)): 
                    origin = (latitude,longitude)
                    coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                    if (place.get('user_ratings_total',0) > 100) and (place.get('rating',0)>0):
                        result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                        if result['status']=='OK':
                            element = result['rows'][0]['elements'][0]
                            if element['status'] == 'OK':
                                distance = element['distance']['text']
                                duration = element['duration']['text']
                            else:
                                distance = "cann't find"
                                duration = "cann't find"
                        Restaurants.objects.create(
                            name = place.get('name','No Name'),
                        status = place.get('business_status','default'),
                        address = place.get('vicinity','unknown'),
                        coordinates = coordinate,
                        types = place.get('types',[]),
                        rating = place.get('rating',0),
                        user_rating = place.get('user_ratings_total',0),
                        Travel_Distance = distance,
                        Travel_Time = duration,
                        source_location = source_location
                        )
                    else:
                        result['status'] == 'Error'
                    
            return redirect('result')    
    else:
        form = LocationForm()

    return render(request, 'googlelocation/home.html',{'form':form})
def result(request):
    sourcelocation = SourceLocation.objects.distinct()
    competitors = Competitor.objects.distinct()
    supermarkets = SuperMarket.objects.distinct()
    publicservices = PublicServices.objects.distinct()
    apartments = Apartments.objects.distinct()
    retails = Retails.objects.distinct()
    restaurants = Restaurants.objects.distinct()
    context = {
        'sourcelocation':sourcelocation, #done
        'competitors':competitors,       #done
        'publicservices':publicservices, #done
        'retails':retails,
        'restaurants': restaurants,      #done
        'apartments': apartments,        #done
        'supermarkets': supermarkets,    #done
    }
    
    return render(request, 'googlelocation/result.html', context)

