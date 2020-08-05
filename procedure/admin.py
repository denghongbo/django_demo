from django.contrib import admin
from procedure.models import Procedure


class ProcedureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Procedure, ProcedureAdmin)

