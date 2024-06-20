from django.db import models


# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre_user = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_user


class Tiquete(models.Model):
    id_tiquete = models.AutoField(primary_key=True)
    clase_tiquete = models.CharField(max_length=30)
    asiento_tiquete = models.CharField(max_length=30)
    valor_tiquete = models.IntegerField()
    user_tiquete = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_tiquete


class Vuelo(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    fecha_vuelo = models.DateField(default="01-01-2020")  # cambiar

    def __str__(self):
        return self.id_vuelo


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    tiquete_reserva = models.ForeignKey(Tiquete, on_delete=models.DO_NOTHING)
    vuelo_reserva = models.ForeignKey(Vuelo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_reserva
