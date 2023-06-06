from django.contrib import admin
from apps.accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "name", "is_tc", "is_admin"]
    list_filter = ["is_admin", "is_tc"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "phone_no"]}),
        ("Policy", {"fields": ["is_tc"]}),
        ("Permissions", {"fields": ["is_admin", "groups", "user_permissions"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "is_tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["id"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
