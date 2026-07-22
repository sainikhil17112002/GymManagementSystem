from django.contrib import admin

admin.site.site_header = "GPISC Gym Management"
admin.site.site_title = "GPISC Admin"
admin.site.index_title = "Welcome to GPISC Dashboard"
from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "member_id",
        "first_name",
        "last_name",
        "phone",
        "status",
    )

    search_fields = (
        "member_id",
        "first_name",
        "last_name",
        "phone",
    )

    list_filter = (
        "status",
        "gender",
    )