from django import forms
from app_prueba.models import Pregunta, Respuesta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta

        fields = [
            'asunto',
            'descripcion',
        ]
        labels = {
            'asunto' : 'asunto',
            'descripcion' : 'descripcion'
        }
        widgets = {
            'asunto' : forms.TextInput(),
            'descripcion' : forms.TextInput(),
        }


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta

        fields = [
            'pregunta',
            'contenido',
            'mejor_respuesta',
        ]
        labels = {
            'pregunta' : 'Pregunta',
            'contenido' : 'Contenido',
            'mejor_respuesta' : 'Mejos Respuesta',
        }

        widgets = {
            'pregunta' : forms.Select(),
            'contenido': forms.TextInput(),
            'mejor_respuesta' : forms.CheckboxInput(),
        }
