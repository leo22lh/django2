from django.shortcuts import render, redirect
from app_prueba.forms import PreguntaForm, RespuestaForm
from app_prueba.models import Pregunta, Respuesta
from django.views.generic import CreateView,ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def PreguntaView(request):
    if request.method == 'POST' :
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PreguntaForm()
    return render(request, 'pregunta.html', {'form' : form})

def PreguntaListarView(request):
    preguntas = Pregunta.objects.all()
    contexto = {'preguntas' : preguntas}
    return render(request, 'pregunta_listar.html', contexto)

def PreguntaEditView(request, id_pregunta):
    pregunta = Pregunta.objects.get(id=id_pregunta)
    if request.method == 'GET':
        form = PreguntaForm(instance=pregunta)
    else:
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'pregunta.html', {'form': form})

def PreguntaDeleteView(request, id_pregunta):
    pregunta = Pregunta.objects.get(id=id_pregunta)
    if request.method == 'GET':
        pregunta.delete()
    return redirect('pregunta_listar')
class RespuestaCreateView(CreateView):
    model = Respuesta
    form_class = RespuestaForm
    template_name = 'respuesta_create.html'
    success_url = reverse_lazy('respuesta_listar')

class RespuestaListarView(ListView):
    model = Respuesta
    template_name = 'respuesta_listar.html'

class RespuestaEditarView(UpdateView):
    model = Respuesta
    template_name = 'respuesta_create.html'
    form_class = RespuestaForm
    success_url = reverse_lazy('respuesta_listar')

class RespuestaDeleteView(DeleteView):
    model = Respuesta
    template_name = 'respuesta_delete.html'
    success_url = reverse_lazy('respuesta_listar')

class PRCreateView(CreateView):
    model = Pregunta
    template_name = 'pr_create.html'
    form_class = PreguntaForm
    second_form_class = RespuestaForm
    success_url = reverse_lazy('respuesta_listar')

    def get_context_data(self, **keywards):
        context = super(PRCreateView, self).get_context_data(**keywards)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    def post(self, request, *args, **keywards):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            pr = form.save(commit=False)
            pr.respuesta = form2.save()
            pr.save()
            return HttpResponseRedirect(self.get_success_url()
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
