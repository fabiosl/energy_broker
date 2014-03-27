from django.contrib import admin
from energy_app.models import *
admin.site.register(Query)
admin.site.register(CloudProvider)
admin.site.register(PowerProducer)
admin.site.register(PowerChunk)
admin.site.register(Consumer)