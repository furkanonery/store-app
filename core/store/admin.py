from django.contrib import admin
from store.models import Cart, CartItem, Category, Order, OrderItem, Product, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'user__email')
    fields = ('user', 'profile_picture', 'phone_number', 'address', 'birth_date', 'bio')

class CartItemInline(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [CartItemInline]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass