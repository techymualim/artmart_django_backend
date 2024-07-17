from django import forms
from .models import Details

class ArtistStep1Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['store_name', 'store_email']

class ArtistStep2Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['address', 'city', 'state', 'postal_code', 'country']

class ArtistStep3Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['shop_address', 'shop_city', 'shop_state', 'shop_postal_code', 'shop_country']

class ArtistStep4Form(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['shop_type', 'art_specialization']
