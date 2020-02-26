from django import forms
from .models import Reservation


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

class RoomForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "full_name",
            "email",
            "check_in",
            "check_out",
        ]