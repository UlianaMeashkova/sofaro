from django.contrib import admin

from products.models import Product, Booking, Hotels, ProductImage, Comment, Score


class BookingAdminInline(admin.StackedInline):
    model = Booking

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "country", "description", "created_at")
    fields = ("title", "image", "price","price_usd", "country", "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = (BookingAdminInline, ProductImageAdmin,)


    def save_form(self, request, form, change):

        return super().save_form(request, form, change)

class Meta:
    model=Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "product__title")

    def save_form(self, request, form, change):

        return super().save_form(request, form, change)

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
    
@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):  
    list_display = ('name', 'email', 'post', 'created', 'active')  
    list_filter = ('active', 'created', 'updated')  
    search_fields = ('name', 'email', 'body')
    

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass

    
