from django.shortcuts import render
from . import forms
from .models import Room, Reservation
from datetime import timedelta, date

# Create your views here.
def home(request):
    return render(request, 'index.html')

def rooms(request):
	form = forms.CheckAvailability(request.POST or None)
	form_success = forms.SingleRoomForm(request.POST or None)
	context = {"form": form}
	if form.is_valid():
		instance = form.save(commit=False)
		start_date = instance.arrival_date
		end_date = instance.departure_date + timedelta(days=1)
		reservation_days = end_date - instance.arrival_date
		for i in range(reservation_days.days):
			day = start_date + timedelta(days=i)
			if day in Room.objects.filter(arrival_date__range=[start_date, end_date]):
				messages.warning(request, 'Unfortunately the rooms have all been booked for {} please pick another date to come visit us'.format(day))
				form = forms.CheckAvailability()
		else:
			return render(request, "bookingssingle.html", {"form": form_success})		

	return render(request, "rooms.html", context) 


def aboutus(request):
	return render(request, "about.html")

def contact(request):
	return render(request, "contact.html")


def singleroom(request):
	form = forms.SingleRoomForm(request.POST or None)
	title = "Single Room"
	price = 50

	if form.is_valid():
		instance = form.save(commit=False)
		reservation_days = instance.departure_date - instance.arrival_date
		price_duration = price * reservation_days.days


		if instance.arrival_date in Room.values("arrival_date"):
			Room.num_of_rooms -= 1
			if Room.num_of_rooms == 0:
				context = {
					"form": form,
					"error_message": "The number of rooms have been fully booked for {} \n please try on another date".format(instance.arrival_date)
				}
				instance.delete()
				return render(request, "singleroom.html", context)
				
			instance.save()	
			return render(request, "index.html")

	return render(request, "singleroom.html", {"form": form})


def doubleroom(request):
	form = forms.RoomForm(request.POST or None)
	title = "Double Room"
	price = 50

	if form.is_valid():
		instance = form.save(commit=False)
		reservation_days = instance.departure_date - instance.arrival_date
		price_duration = price * reservation_days.days


		if instance.arrival_date in models.Room.values("arrival_date"):
			Room.num_of_rooms -= 1
			if Room.num_of_rooms == 0:
				context = {
					"form": form,
					"error_message": "The number of rooms have been fully booked for {} \n please try on another date".format(instance.arrival_date)
				}
				instance.delete()
				return render(request, "doubleroom.html", context)
				
			instance.save()	
			return render(request, "index.html")

	return render(request, "doubleroom.html", {"form": form})


def executiveroom(request):
	form = forms.RoomForm(request.POST or None)
	title = "Executive Room"
	price = 50

	if form.is_valid():
		instance = form.save(commit=False)
		reservation_days = instance.departure_date - instance.arrival_date
		price_duration = price * reservation_days.days


		if instance.arrival_date in models.Room.values("arrival_date"):
			Room.num_of_rooms -= 1
			if Room.num_of_rooms == 0:
				context = {
					"form": form,
					"error_message": "The number of rooms have been fully booked for {} \n please try on another date".format(instance.arrival_date)
				}
				instance.delete()
				return render(request, "executiveroom.html", context)
				
			instance.save()	
			return render(request, "index.html")

	return render(request, "executiveroom.html", {"form": form})

def conferenceroom(request):
	form = forms.RoomForm(request.POST or None)
	title = "Conference Room"
	price = 50

	if form.is_valid():
		instance = form.save(commit=False)
		reservation_days = instance.departure_date - instance.arrival_date
		price_duration = price * reservation_days.days


		if instance.arrival_date in models.Room.values("arrival_date"):
			Room.num_of_rooms -= 1
			if Room.num_of_rooms == 0:
				context = {
					"form": form,
					"error_message": "The number of rooms have been fully booked for {} \n please try on another date".format(instance.arrival_date)
				}
				instance.delete()
				return render(request, "conferenceroom.html", context)
				
			instance.save()	
			return render(request, "index.html")

	return render(request, "conferenceroom.html", {"form": form})	


	from django.shortcuts import redirect

def confirm(request, pk = None):
	form = ConfirmForm(request.POST or None)
	if form.is_valid:
		instance = form.save(commit=False)
        if pk:
            invalid_dates = False
            #get the room 
            room = Room.objects.get(pk = pk)
            guest_id = instance.user
            check_in = instance.session['check_in'] 
            check_out = instance.session['check_out']

            # check whether the dates are valid
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(room=room, check_in__lte=check_in, check_out__gte=check_in).exists()

            # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(room=room, check_in__lte=check_out, check_out__gte=check_out).exists()

            case_3 = Reservation.objects.filter(room=room, check_in__gte=check_in, check_out__lte=check_out).exists()


            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                  return render(request, "bookingssingle.html", {"errors": "This room is not available on your selected dates"})                  

             # dates are valid             
             reservation = Reservation(
             check_in = reservation.check_in, 
             check_out = reservation.check_out,
             room_id = room.id,
             guest_id = guest_id.id
             )

             reservation.save()

             #redirect to success page (need to define this as a separate view)
             return redirect("success")


      return render(request, "bookingssingle.html", args)


# 			