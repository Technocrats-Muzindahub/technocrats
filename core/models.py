from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


now = timezone.now
end = timezone.now() + timezone.timedelta(days=2)
room_choices = [
		('single_room', 'Single Room'),
		('double_room', 'Double Room'),
		('executive_room', 'Executive Room'),
	]



class Reservation(models.Model):
	room_type = models.CharField(max_length=30, choices=room_choices, default=room_choices[1])
	check_in = models.DateField(default=timezone.now)
	check_out = models.DateField(default=end)
	
	class Meta:
		verbose_name = 'Reservation'
		verbose_name_plural = 'Reservations'

