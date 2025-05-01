from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # This tells Django which model to use for the UserAdmin.
    model = User
    # These are the fields displayed on the list page of the admin interface.
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    # These are the fields that can be used as filters in the list view.
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    # This allows searching by username and email in the admin list view.
    search_fields = ('email', 'username')
    # This determines the default ordering of the list.
    ordering = ('-date_joined',)

    # These are the fields displayed when adding or editing a user.
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('role', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
       
    )
    
    # These are the fields shown when creating a user. The 'password1' and 'password2' are for user password confirmation.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser')
        }),
    )
    
    # Ensuring that the password is hashed before saving it.
    def save_model(self, request, obj, form, change):
        if not obj.password:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

    # Since you don't have 'groups' and 'user_permissions' fields, you can omit this or leave it empty.
    filter_horizontal = ()

# Register the User model with the custom UserAdmin
admin.site.register(User, CustomUserAdmin)
