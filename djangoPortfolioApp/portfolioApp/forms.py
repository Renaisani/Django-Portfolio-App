from django.forms import ModelForm
from django.db import models
from .models import ContactEntry

class ContactForm(ModelForm):
    class Meta:
        model = ContactEntry
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['company'].required = False