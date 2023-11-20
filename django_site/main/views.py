from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm


# Create your views here.
def about(request):
    return render(request, 'main/about.html')


def thanks(request):
    return render(request, 'main/thanks.html')


def create_appointment(request):
    error = ''
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            error = 'Форма была неверной'

    form = AppointmentForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/index.html', context)
