from django import forms

class LocationForm(forms.Form):
    location  = forms.CharField(label='Location (latitude,longitude)',
                                max_length=100,
                                widget=forms.TextInput(attrs={'placeholder':'latitude,longitude'}))
    radius = forms.FloatField(label="Enter the radius(Meters)",min_value=1,
                              widget=forms.TextInput(attrs={'placeholder': 'Radius in meters'}))
