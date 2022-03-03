from dataclasses import fields
from rest_framework import routers, serializers, viewsets

#importancion de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    model = PrimerTabla
    fields = ("nombre","edad")
