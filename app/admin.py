from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import ExampleModel, Profile


class ExampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '200'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4})},
    }


admin.site.register(Profile)
admin.site.register(ExampleModel, ExampleModelAdmin)
