from django.contrib import admin

from myapp.models import CryptoModel


admin.site.register(CryptoModel)

# @admin.register(CryptoModel)
# class CryptoAdmin(admin.ModelAdmin):
#
#     def __str__(self):
#         return


# Register your models here.
