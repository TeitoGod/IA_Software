from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'nombre_user')
    search_fields = ['id_user', 'nombre_user']


@admin.register(Tiquete)
class TiqueteAdmin(admin.ModelAdmin):
    list_display = ('id_tiquete', 'user_tiquete')
    search_fields = ['id_tiquete', 'user_tiquete']

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('id_vuelo', 'fecha_vuelo')
    search_fields = ['id_vuelo', 'user_vuelo']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id_reserva', 'tiquete_reserva', 'vuelo_reserva')
    search_fields = ['id_reserva', 'tiquete_reserva', 'vuelo_reserva']