from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    starting_value = models.DecimalField(max_digits=10, decimal_places=2)
    auction_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="won", null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.created_at.tzinfo:
            self.created_at = timezone.make_aware(self.created_at)
        super().save(*args, **kwargs)


class Watch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchList")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchers")
    def __str__(self):
        return f"user {self.user} is watching listing {self.listing}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.created_at.tzinfo:
            self.created_at = timezone.make_aware(self.created_at)
        super().save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=512)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.created_at.tzinfo:
            self.created_at = timezone.make_aware(self.created_at)
        super().save(*args, **kwargs)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # Optional

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")  # "Pending", "Success", "Failed"
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.listing.title} - {self.status}"
    

