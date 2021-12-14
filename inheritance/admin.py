from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Staff)

admin.site.register(Person)
admin.site.register(MyPerson)

admin.site.register(Place)
admin.site.register(Restaurant)
