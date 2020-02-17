from django import forms
from django.contrib.auth.models import User
from .models import Reservation
from django.db import models


class AvailabilityForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = [
			"room_type",
			"check_in",
			"check_out",

		]
		widgets = {
			'check_in': forms.DateInput(format='%m/%d/%Y'),
			'check_out': forms.DateInput(format='%m/%d/%Y'),
		}		