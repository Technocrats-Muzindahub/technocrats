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

# class Room(models.Model):
# 	name = models.CharField(max_length=50, blank=False)
# 	surname = models.CharField(max_length=50, blank=True)
# 	email = models.EmailField()
# 	room_type = models.CharField(max_length=30, choices=room_choices, default=room_choices[1])
# 	arrival_date = models.DateField(default=now)
# 	departure_date = models.DateField(default=end)
# 	num_of_rooms = 4	

# 	def __str__(self):
# 		return "{} {} | {} | {} - {}".format(self.name, self.surname, self.email, self.arrival_date, self.departure_date)

class Room(models.Model):

   name = models.CharField(max_length = 200)
   room_type = models.CharField(max_length=30, choices=room_choices, default=room_choices[1])
   # img = models.ImageField(upload_to='Pictures')
   desc = models.TextField()
   price = models.IntegerField()
   number_of_people = models.PositiveIntegerField()

   def __str__(self):
       return self.name

   class Meta:
       verbose_name = 'Room'
       verbose_name_plural = 'Rooms'

 class Reservation(models.Model):

    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
       verbose_name = 'Reservation'
       verbose_name_plural = 'Reservations'

