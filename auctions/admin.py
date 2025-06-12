from django.contrib import admin

from .models import Feedback, Payment, User, Listing, Watch, Bid, Comment

# Register your models here.
class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "value")
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "comment")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title")

class WatchAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing")

admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(User)
admin.site.register(Watch, WatchAdmin)
admin.site.register(Feedback)
# admin.site.register(Category)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "amount", "razorpay_payment_id", "status", "created_at")
    search_fields = ("user__username", "listing__title", "payment_id", "status")
    list_filter = ("status", "created_at")

admin.site.register(Payment, PaymentAdmin)