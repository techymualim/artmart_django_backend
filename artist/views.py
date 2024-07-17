from django.shortcuts import render, redirect
from django.urls import reverse
from formtools.wizard.views import SessionWizardView
from .forms import ArtistStep1Form, ArtistStep2Form, ArtistStep3Form, ArtistStep4Form
from .models import Details
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

FORMS = [
    ("step1", ArtistStep1Form),
    ("step2", ArtistStep2Form),
    ("step3", ArtistStep3Form),
    ("step4", ArtistStep4Form),
]

TEMPLATES = {
    "step1": "registration/artist_step1.html",
    "step2": "registration/artist_step2.html",
    "step3": "registration/artist_step3.html",
    "step4": "registration/artist_step4.html",
}

class ArtistWizard(SessionWizardView):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # Create a new Details instance and associate it with the logged-in user
        details_data = {}
        for form in form_list:
            details_data.update(form.cleaned_data)

        user = self.request.user
        Details.objects.create(user=user, **details_data)
        
        return redirect('/')  # Redirect to a success page after the form is complete
