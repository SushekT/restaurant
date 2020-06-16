from django.shortcuts import render
from .models import Reservation
# Create your views here.
from .form import ReserveTableForm


def reservetable(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()


    context = {'form': reserve_form,}

    return render(request, 'Reservation/reservation.html', context)
