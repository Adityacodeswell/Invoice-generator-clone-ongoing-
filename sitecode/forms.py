from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Service , Add_service

class UserLogin(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            'username': 'UserID',
            'password': 'Password'
        }

    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
class ClientData(forms.ModelForm):
    class Meta:
        model = Add_service
        fields = ('client', 'comp2_name', 'handle_by', 'email', 'phone', 'account')
        
        def __init__(self, *args, **qwargs):
            super().__init__(*args, **qwargs)
            self.fields['service'].queryset = Service.objects.none()

            if 'client' in self.data:
                try:
                    client_id = int(self.data.get('client'))
                    self.fields['service'].queryset = Service.objects.filter(client_id = client_id).order_by('comp2_name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['service'].queryset = self.instance.client.service_set.order_by('comp2_name')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['client', 'description', 'quantity', 'amount']

    def __ini__(self, *args, **qwargs):
        super(Service, self).__init__(*args, **qwargs)

        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'