from django.contrib import admin
from .models import Team, About, Services, Portfolio, Clients
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sort')
    list_editable = ('description', 'sort')
    search_fields = ('name',)
    list_filter = ('sort',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_src_tag', 'name', 'client', 'category', 'date', 'description', 'sort')
    list_editable = ('category', 'description', 'sort')
    search_fields = ('name', 'client')
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image_out:
            return mark_safe(f"<img src='{obj.image_out.url}' width=50 height=50>")

    image_src_tag.short_description = 'Portfolio image'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'date', 'description', 'sort')
    list_editable = ('date', 'description', 'sort')
    search_fields = ('name', 'date')
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'About image'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'position', 'facebook', 'twitter', 'linkedin', 'sort')
    list_editable = ('position', 'facebook', 'twitter', 'linkedin', 'sort')
    search_fields = ('name', 'position')
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Team image'


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'link', 'sort')
    list_editable = ('link', 'sort')
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Client image'