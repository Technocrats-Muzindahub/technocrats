from django.shortcuts import get_object_or_404, render, redirect
from . import forms
from .models import Reservation
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')


def rooms(request):
    form = forms.AvailabilityForm()
    context = {"form":form}
    reservation = Reservation
    if request.method == 'POST':
        form = forms.AvailabilityForm(request.POST or None)
        if form.is_valid:
            reserve = form.save(commit=False)
            reserve.reservation = reservation
            check_in = reserve.check_in
            check_out = reserve.check_out
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(check_in__lte=check_in, check_out__gte=check_out).exists()

            # case 2: room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(check_in__lte=check_out, check_out__gte=check_out).exists()

            # case3: room is booked in a date which lies between the two requested check-in/check-out dates
            case_3 = Reservation.objects.filter(check_in__gte=check_in, check_out__lte=check_out).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                return render(request, "availability.html",
                              {"errors": "This room is not available on your selected dates", "form": form})
            # else dates are valid

            reserve.save()
            messages.add_message(request, messages.SUCCESS, 'Room is available for your stay here')
            return redirect('/complete_booking')

    return render(request, "rooms.html", context)


def aboutus(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def singleroom(request):
    form = forms.AvailabilityForm()
    context = {"form":form}
    reservation = Reservation
    if request.method == 'POST':
        form = forms.AvailabilityForm(request.POST or None)
        if form.is_valid:
            reserve = form.save(commit=False)
            reserve.reservation = reservation
            check_in = reserve.check_in
            check_out = reserve.check_out
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(check_in__lte=check_in, check_out__gte=check_out).exists()

            # case 2: room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(check_in__lte=check_out, check_out__gte=check_out).exists()

            # case3: room is booked in a date which lies between the two requested check-in/check-out dates
            case_3 = Reservation.objects.filter(check_in__gte=check_in, check_out__lte=check_out).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                return render(request, "availability.html",
                              {"errors": "This room is not available on your selected dates", "form": form})
            # else dates are valid

            reserve.save()
            messages.add_message(request, messages.SUCCESS, 'Room is available for your stay here')
            return redirect('/complete_booking')

    return render(request, "singleroom.html", context)


def doubleroom(request):
    form = forms.AvailabilityForm()
    context = {"form":form}
    reservation = Reservation
    if request.method == 'POST':
        form = forms.AvailabilityForm(request.POST or None)
        if form.is_valid:
            reserve = form.save(commit=False)
            reserve.reservation = reservation
            check_in = reserve.check_in
            check_out = reserve.check_out
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(check_in__lte=check_in, check_out__gte=check_out).exists()

            # case 2: room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(check_in__lte=check_out, check_out__gte=check_out).exists()

            # case3: room is booked in a date which lies between the two requested check-in/check-out dates
            case_3 = Reservation.objects.filter(check_in__gte=check_in, check_out__lte=check_out).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                return render(request, "availability.html",
                              {"errors": "This room is not available on your selected dates", "form": form})
            # else dates are valid

            reserve.save()
            messages.add_message(request, messages.SUCCESS, 'Room is available for your stay here')
            return redirect('/complete_booking')

    return render(request, "doubleroom.html", context)


def executiveroom(request):
    form = forms.AvailabilityForm()
    context = {"form":form}
    reservation = Reservation
    if request.method == 'POST':
        form = forms.AvailabilityForm(request.POST or None)
        if form.is_valid:
            reserve = form.save(commit=False)
            reserve.reservation = reservation
            check_in = reserve.check_in
            check_out = reserve.check_out
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(check_in__lte=check_in, check_out__gte=check_out).exists()

            # case 2: room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(check_in__lte=check_out, check_out__gte=check_out).exists()

            # case3: room is booked in a date which lies between the two requested check-in/check-out dates
            case_3 = Reservation.objects.filter(check_in__gte=check_in, check_out__lte=check_out).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                return render(request, "availability.html",
                              {"errors": "This room is not available on your selected dates", "form": form})
            # else dates are valid

            reserve.save()
            messages.add_message(request, messages.SUCCESS, 'Room is available for your stay here')
            return redirect('/complete_booking')

    return render(request, "executiveroom.html", context)


def conferenceroom(request):
    form = forms.AvailabilityForm()
    context = {"form":form}
    reservation = Reservation
    if request.method == 'POST':
        form = forms.AvailabilityForm(request.POST or None)
        if form.is_valid:
            reserve = form.save(commit=False)
            reserve.reservation = reservation
            check_in = reserve.check_in
            check_out = reserve.check_out
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(check_in__lte=check_in, check_out__gte=check_out).exists()

            # case 2: room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(check_in__lte=check_out, check_out__gte=check_out).exists()

            # case3: room is booked in a date which lies between the two requested check-in/check-out dates
            case_3 = Reservation.objects.filter(check_in__gte=check_in, check_out__lte=check_out).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                return render(request, "availability.html",
                              {"errors": "This room is not available on your selected dates", "form": form})
            # else dates are valid

            reserve.save()
            messages.add_message(request, messages.SUCCESS, 'Room is available for your stay here')
            return redirect('/complete_booking')

    return render(request, "conferenceroom.html", context)


def complete_booking(request):
    return render(request, "bookings.html")

		