# coding: utf-8

from django.contrib import admin
from website.ratings.models import Rating


class RatingAdmin(admin.ModelAdmin):
    list_display = ('sandwich', 'kind', 'user', 'score')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Rating, RatingAdmin)
