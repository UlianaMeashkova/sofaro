from django.contrib import admin

from products.models import Product, Booking, Hotels


class BookingAdminInline(admin.StackedInline):
    model = Booking


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "country", "description", "created_at")
    fields = ("title", "image", "price","price_usd", "country", "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = (BookingAdminInline,)


    def save_form(self, request, form, change):

        return super().save_form(request, form, change)



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "product__title")

# # Register your models here.

@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ( "country", "title",  "description", "created_at")
    fields = ("country", "title", "image",  "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    # inlines = (BookingAdminInline,)

    def save_form(self, request, form, change):

        return super().save_form(request, form, change)
    
