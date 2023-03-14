from django.forms import ModelForm
from django.db import models
from .models import ContactEntry

class ContactForm(ModelForm):

    company = models.CharField(null=True, blank=True)

    class Meta:
        model = ContactEntry
        fields = "__all__"