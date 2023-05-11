from django.contrib import admin

# Register your models here.
from django.contrib import admin

from users.models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
   list_display = ("user", "first_name", "last_name", "email", "created_at")
#    fields = ("user", "first_name", "last_name", "age" "created_at")
#    readonly_fields = ("created_at",)
#    search_fields = ("first_name", "last_name")

# Register your models here.
