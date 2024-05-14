from django.contrib import admin
from .models import Thought, Recurrence, Tag
# Register your models here.
admin.site.register(Thought)
admin.site.register(Recurrence)
admin.site.register(Tag)