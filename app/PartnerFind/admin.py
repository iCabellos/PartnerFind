from django.contrib import admin
from .models import UserModel, MatchModel, MatchPlayer

admin.site.register(UserModel)


class MatchPlayerInline(admin.TabularInline):
    model = MatchPlayer
    extra = 4


class MatchModelAdmin(admin.ModelAdmin):
    inlines = [MatchPlayerInline]


admin.site.register(MatchModel, MatchModelAdmin)
