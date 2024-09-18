from django.shortcuts import render
from django.http import HttpResponse 
from .forms import LocationForm
from .models import Place
import json
from django import views
import googlemaps


class LocationView(views):
    template_name = 'googlelocation/home.html'
    google_api_key = 'AIzaSyCNJ0iv-Why9tmFmkTZrIVPp_B_qMZYQpg'
    def get(self,request,*args,**kwargs):
        form = LocationForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form = LocationForm(request.POST)
        context = {}
        if form.is_valid():
            location  = form.cleaned_data['location']
            radius = form.cleaned_data['radius']
            try:
                latitude, longitude = map(float,location.strip().split(','))
            except:
                pass


# def home(request):
#     if request.method == 'POST':
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             location = form.cleaned_data['location']
#             radius = form.cleaned_data['radius']
            
#             try:

#                 longitude,latitude = map(float,location.split(','))
#                 Google_API_KEY = 'AIzaSyCNJ0iv-Why9tmFmkTZrIVPp_B_qMZYQpg'

#                 context = {
#                     'longitude':longitude,
#                     'latitude' : latitude,
#                     'radius':radius,
#                     'form' : form,
#                     'success':True,
#                 }
#             except:
#                 context={
#                     'form':form,
#                     'error': 'Invalid location format. Please use "longitide, latitude format."'
#                 }
#         else:
#             context = {
#                 'form': form,
#                 'error': 'Invalid input. Please correct the errors below.'
#             }
        
#     else:
#         form = LocationForm()
#         context = {'form':form}
#     return render(request, 'googlelocation/home.html',context)



