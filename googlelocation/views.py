from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import LocationForm
from .models import SourceLocation, SuperMarket,PublicServices,Competitor,Residentials,Retails,Restaurants,Hotels,Tourist,Education
import json
from django import views
import googlemaps
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
import re
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
            Residentials.objects.all().delete()
            Retails.objects.all().delete()
            Restaurants.objects.all().delete()
            Hotels.objects.all().delete()
            Residentials.objects.all().delete()
            Tourist.objects.all().delete()
            Education.objects.all().delete()
            
            gmaps = googlemaps.Client(key=Google_API_KEY)

            # source database
            source_location = SourceLocation.objects.create(
                Source_lat = latitude,
                Source_lon = longitude)
            # competitors database
            competitor = ['KFC','Burger+King',"McDonald's",'Pizza+Hut',"Domino's"]
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
                pattern = r"McDonald['’]s|Burger\s+King|Pizza\s+Hut|Domino['’]s|KFC"
                if re.search(pattern,place.get('name','NO Name'), re.IGNORECASE):
                    if not Competitor.objects.filter(coordinates=coordinate).exists():
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
            supermarket = ['Mall','Supermarket','Vishal+Mega+mart','Croma','D-mart','Trends','smart+bazaar','Reliance+Digital','department-store']

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
                    if not SuperMarket.objects.filter(coordinates=coordinate).exists():
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

            #Tourist

            
            nearby_tourist = []
            tourists = ['tourist','park','museum']

            for tourist in tourists:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = tourist)
                if places_result['status'] == 'OK':
                    nearby_tourist.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_tourist:
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
                    if not Tourist.objects.filter(coordinates=coordinate).exists():
                        Tourist.objects.create(
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
                
            
            # Education Database

            nearby_education = []
            educations = ['School','Institue','college','University','Inter college']

            for education in educations:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = education)
                if places_result['status'] == 'OK':
                    nearby_education.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_education:
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
                    if not Education.objects.filter(coordinates=coordinate).exists():
                        Education.objects.create(
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
            publicservices = ['Bus Stand','Railway station','Metro','transit-station','Medical']
            
            for public in publicservices:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = public)
                if places_result['status'] == 'OK':
                    nearby_publicservices.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_publicservices:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 200) and (place.get('rating',0)>3):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    if not PublicServices.objects.filter(coordinates=coordinate).exists():
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
            
            
            # Hotels database 
            nearby_hotels = []    
            hotels = ['lodging','Hotels']

            for hotel in hotels:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = hotel)
                if places_result['status'] == 'OK':
                    nearby_hotels.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_hotels:
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
                    if not Hotels.objects.filter(coordinates=coordinate).exists():        
                        Hotels.objects.create(
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

           
           
            #Residential database
            nearby_residentials = [] 
            residentials = ['Appartments','Housing Society','Guest House','flats'] 
            for resident in residentials:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = resident)
                if places_result['status'] == 'OK':
                    nearby_residentials.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_residentials:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 100):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    if not Residentials.objects.filter(coordinates=coordinate).exists() and not Hotels.objects.filter(coordinates=coordinate).exists():
                        Residentials.objects.create(
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
            retails = ['retail shop','store','eletronic-store','salon'] 
            for retail in retails:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = retail)
                if places_result['status'] == 'OK':
                    nearby_retails.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_retails:
                origin = (latitude,longitude)
                coordinate = (place['geometry']['location']['lat'],place['geometry']['location']['lng'])
                if (place.get('user_ratings_total',0) > 200) and (place.get('rating',0)>3):
                    result = gmaps.distance_matrix(origins=[origin], destinations=[coordinate], mode='driving', departure_time='now')
                    if result['status']=='OK':
                        element = result['rows'][0]['elements'][0]
                        if element['status'] == 'OK':
                            distance = element['distance']['text']
                            duration = element['duration']['text']
                        else:
                            distance = "cann't find"
                            duration = "cann't find"
                    if not Retails.objects.filter(coordinates=coordinate).exists() and not SuperMarket.objects.filter(coordinates = coordinate).exists():
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
            restaurants = ['Restaurant','cafe','Bakery']
            for restaurant in restaurants:
                places_result = gmaps.places_nearby(location = (latitude,longitude),radius = radiuss,keyword = restaurant)
                if places_result['status'] == 'OK':
                    nearby_restaurant.extend(places_result.get('results', []))
                else:
                    continue
            for place in nearby_restaurant:
                if place['name'] not in exclude_competitor and (place.get('user_ratings_total',0) > 200) and (place.get('rating',0)>3): 
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
                        if not Restaurants.objects.filter(coordinates=coordinate).exists():
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
    residentials = Residentials.objects.distinct()
    retails = Retails.objects.distinct()
    restaurants = Restaurants.objects.distinct()
    hotels = Hotels.objects.distinct()
    education = Education.objects.distinct()
    tourist = Tourist.objects.distinct()
    competitors_json = json.dumps(list(competitors.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    supermarkets_json = json.dumps(list(supermarkets.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    publicservices_json = json.dumps(list(publicservices.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    residentials_json = json.dumps(list(residentials.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    retails_json = json.dumps(list(retails.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    restaurants_json = json.dumps(list(restaurants.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    hotels_json = json.dumps(list(hotels.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    education_json = json.dumps(list(education.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    tourist_json = json.dumps(list(tourist.values('name', 'coordinates', 'rating', 'Travel_Distance', 'Travel_Time')))
    context = {
        'sourcelocation':sourcelocation, #done
        'competitors':competitors,       #done
        'publicservices':publicservices, #done
        'retails':retails,               #done
        'restaurants': restaurants,      #done
        'residentials': residentials,    #done
        'supermarkets': supermarkets,    #done
        'education':education,           #done
        'hotels':hotels,                 #done
        'tourist':tourist,               #done
        'competitors_json': mark_safe(competitors_json),
        'supermarkets_json':mark_safe(supermarkets_json),
        'publicservices_json':mark_safe(publicservices_json),
        'residentials_json':mark_safe(residentials_json),
        'retails_json':mark_safe(retails_json),
        'restaurants_json':mark_safe(restaurants_json),
        'hotels_json':mark_safe(hotels_json),
        'education_json':mark_safe(education_json),
        'tourist_json':mark_safe(tourist_json)
    }
    print(type(competitors_json))
    return render(request, 'googlelocation/result.html', context)