from django.db import models

class Pregunta(models.Model):
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto

    def publicado_hoy(self):
        return self.fecha_publicacion().date() == timezone.now().date()


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    contenido = models.TextField()
    mejor_respuesta = models.BooleanField("respuesta preferida", default=False)

    def __str__(self):
        return self.contenido
