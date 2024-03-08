from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms


class MqForm(ModelForm):
    class Meta:
        model = models.Mq
        fields = ('idmqtt', 'nom', 'piece', 'emplacement')
        labels = {
            'idmqtt': _('Id du MQTT'),
            'nom' : _('Nom du capteur'),
            'piece' : _('Pièce') ,
            'emplacement' : _('Emplacement du capteur')
        }
        widgets = {
            'emplacement': TextInput(attrs={'readonly': 'readonly', 'style': 'cursor: not-allowed'}),
        }

class DoForm(ModelForm):
    class Meta:
        model = models.Do
        fields = ('mqid', 'date', 'heure', 'temp', 'mqnom')
        labels = {
            'mqid' : _('Mqtt id '),
            'date' : _('Date ') ,
            'heure' : _('Heure '),
            'temp' : _('Température '),
            'mqnom' : _('nom mq id')
    }
        
class F5Form(forms.Form):
    x = forms.IntegerField(label='Délai de rafraîchissement (en millisecondes)')