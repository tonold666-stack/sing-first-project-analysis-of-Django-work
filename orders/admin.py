# from django.contrib import admin

# import orders
# from orders.models import Order, OrderItem

# # admin.site.register(Order)
# # admin.site.register(OrderItem)

# class OrderItemTabulareAdmin(admin.TabularInline):
#     model = OrderItem
#     fields = "product", "name", "price", "quantity"
#     search_fields = (
#         "product",
#         "name",
#     )
#     extra = 0


# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = "order", "product", "name", "price", "quantity"
#     search_fields = (
#         "order",
#         "product",
#         "name",
#     )


# class OrderTabulareAdmin(admin.TabularInline):
#     model = Order
#     fields = (
#         "requires_delivery",
#         "status",
#         "payment_on_get",
#         "is_paid",
#         "created_timestamp",
#     )

#     search_fields = (
#         "requires_delivery",
#         "payment_on_get",
#         "is_paid",
#         "created_timestamp",
#     )
#     readonly_fields = ("created_timestamp",)
#     extra = 0

#     @admin.register(Order)
#     class OrderAdmin(admin.ModelAdmin):
#         list_display = (
#             "id",
#             "user",
#             "requires_delivery",
#             "status",
#             "payment_on_get",
#             "is_paid",
#             "created_timestamp",
#         )

#         search_fields = (
#             "id",
#         )
#         readonly_fields = ("created_timestamp",)
#         list_filter = (
#             "requires_delivery",
#             "status",
#             "payment_on_get",
#             "is_paid",
#         )
#         readonly_fields = ("created_timestamp",)
#         list_filter = (
#             "requires_delivery",
#             "status",
#             "payment_on_get",
#             "is_paid",
#             "created_timestamp",
#         )

from django.contrib import admin
from orders.models import Order, OrderItem

# 1. Инлайн для товаров внутри заказа
class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("product", "name", "price", "quantity")
    extra = 0

# 2. Админка для товаров (если хочешь смотреть их отдельно)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "name", "price", "quantity")
    search_fields = ("order__id", "product__name", "name") # Используй __ для поиска по связанным полям

# 3. Главная админка заказа
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "id",
        "phone_number", # Поиск по номеру телефона обычно полезнее
    )
    
    readonly_fields = ("created_timestamp",)
    
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    
    # Добавляем товары прямо в карточку заказа
    inlines = (OrderItemTabulareAdmin,)

# Если тебе ОЧЕНЬ нужно видеть заказы инлайном где-то еще (например в профиле пользователя), 
# тогда оставь это, но вынеси отдельно:
class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = ("requires_delivery", "status", "payment_on_get", "is_paid", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 0
