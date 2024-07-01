from django.contrib import admin
from .models import Gantt

from django.contrib import admin
from .models import Gantt

@admin.register(Gantt)
class GanttAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'finish_date')
    # Remova qualquer referência ao campo responsible aqui
