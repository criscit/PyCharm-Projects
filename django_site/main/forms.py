from .models import Appointment
from django.forms import ModelForm, TextInput, EmailField, DateTimeField


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['is_approved']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['comments'].required = False
        # widgets = {'first_name': TextInput(attrs={'class': 'form-control',
        #                                           'placeholder': 'Введите Ваше имя'}),
        #            'second_name': TextInput(attrs={'class': 'form-control',
        #                                            'placeholder': 'Введите Вашу Фамилию'}),
        #            # 'email': EmailField(attrs={'class': 'form-control',
        #            #                            'placeholder': 'Введите Ваш email'}),
        #            # 'date_time': DateTimeField(attrs={'class': 'form-control',
        #            #                                   'placeholder': 'Введите дату'}),
        #            }
