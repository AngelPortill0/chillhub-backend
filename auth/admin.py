from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth.forms import CustomUserChangeForm, CustomUserCreationForm

from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    readonly_fields = ("uuid",)
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            "User Data",
            {
                "fields": (
                    "uuid",
                    "username",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_email_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": (
    #                 "uuid",
    #                 "username",
    #                 "email",
    #                 "password1",
    #                 "password2",
    #                 "is_staff",
    #                 "is_active",
    #                 "groups",
    #                 "user_permissions",
    #                 "created_at",
    #                 "updated_at",
    #                 "last_login_at",
    #             ),
    #         },
    #     ),
    # )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
