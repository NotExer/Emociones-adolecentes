from django.db import models



emociones = [
    ('', 'Seleccionar'),
    ('Felicidad','Felicidad'),
    ('Tristeza','Tristeza'),
    ('Enojo','Enojo'),
    ('Miedo','Miedo'),
    ('Sorpresa','Sorpresa'),
    ('Asco','Asco'),
    ('Confusión','Confusión'),
    ('Interés','Interés'),
    ('Aburrimiento','Aburrimiento'),
    ('Culpa','Culpa'),
    ('Vergüenza','Vergüenza'),
    ('Amor','Amor'),
    ('Gratitud','Gratitud'),
    ('Esperanza','Esperanza'),
    ('Ansiedad','Ansiedad'),
    ('Frustración','Frustración'),
    ('Alivio','Alivio'),
    ('Orgullo','Orgullo'),
    ('Empatía','Empatía'),
    ('Admiración','Admiración'),
    ('Confianza','Confianza'),
    ('Soledad','Soledad'),
    ('Desesperación','Desesperación'),

]


class Cliente(models.Model):
    EmocionID = models.AutoField(primary_key=True)
    Emociones = models.CharField(max_length=20, choices=emociones, blank=False, null=False)
    Comentario = models.TextField(blank=True, null=True)
    UltimaModificacion = models.DateTimeField(auto_now=True)
