from django.contrib import admin
from .models import *

# Register your models here.
# =================================================================
# *** accounts ***
admin.site.register(User)

# =================================================================
# *** skills  ***
admin.site.register(Skill)
# admin.site.register(Photo)
# admin.site.register(Adoption)

# =================================================================
# ***   ***
