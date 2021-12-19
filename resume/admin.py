from django.contrib import admin
from .models import State,Name
# Register your models here.
class NameInline(admin.TabularInline):
    #model = Name
    pass
@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
   list_display = ["first_name", "last_name", "date_of_birth","date_updated", "date_created"]
   list_filter = ["first_name","date_updated"]
   fieldsets = (
       ("Names",
       {"fields":("first_name","last_name")}),

       ("Others",
       {
          "fields":("state_of_origin","summary","date_of_birth") 
       })

   )
   #inlines = [NameInline]
admin.site.register(State)
#admin.site.register(Name, NameAdmin)
