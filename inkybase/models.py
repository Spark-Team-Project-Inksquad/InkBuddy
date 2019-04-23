from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#Exceptions
from django.core.exceptions import ObjectDoesNotExist

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# OS
import os

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, unique = True)
    # may replace with specific field
    # with validation
    profile_img = models.ImageField(upload_to = 'media/uploads/', null = True)
    phone_number = models.CharField(blank=True, max_length = 11)
    bio = models.TextField(blank = True)

    # is the account a vendor or not?
    isVendor = models.BooleanField(default = False)

    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, self.uploaded_file.name)

        if (os.path.isfile(file_path)):
            os.remove(file_path)

        super(Account, self).delete(*args, **kwargs)

    def __str__(self):
        return self.user.username + " Account"

# Create an Account if a user is created
@receiver(post_save, sender=User)
def on_user_save(sender, instance, **kwargs):
    try:
        print (instance)
        auth_account = Account.objects.get(user = instance)
    except ObjectDoesNotExist as e:
        print ("No account exists. One will be created")
        new_account = Account(user = instance, profile_img = None)
        new_account.save()
        print ("USER ACCOUNT CREATED")

# Favorite Vendors of a user
class FavoriteVendor(models.Model):
    owner = models.ForeignKey(Account, on_delete = models.CASCADE)
    vendor = models.ForeignKey(Account, on_delete = models.CASCADE, related_name = 'accounts_favorited')

# Review of a Vendor
class VendorReview(models.Model):
    author = models.ForeignKey(Account, on_delete = models.CASCADE, related_name = "vendor_reviews")
    reviewed_vendor = models.ForeignKey(Account, on_delete = models.CASCADE)

    score = models.IntegerField(default = 0)

# Document itself
class Document(models.Model):
    owner = models.ForeignKey(Account, on_delete = models.CASCADE)
    uploaded_file = models.FileField(upload_to = 'uploads')

    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, self.uploaded_file.name)

        if (os.path.isfile(file_path)):
            os.remove(file_path)

        super(Document, self).delete(*args, **kwargs)

# Vendor Spec
class VendorSpec(models.Model):
    owner = models.ForeignKey(Account, on_delete = models.CASCADE)
    type_of_print = models.CharField(max_length = 255)
    material = models.CharField(max_length = 255)
    transport = models.CharField(max_length = 255)
    price_per = models.DecimalField(max_digits = 5, decimal_places = 2)
    additional_info = models.TextField()

# TODO Order model
class Order(models.Model):

    pass

class Chat(models.Model):
    pass

class ChatMessage(models.Model):
    pass
