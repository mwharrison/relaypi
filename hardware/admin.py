from django.contrib import admin
from models import Relay


class RelayAdmin(admin.ModelAdmin):
    list_display = ('name', 'gpio_id' )
    save_on_top = True
    

admin.site.register(Relay, RelayAdmin)