from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MemberChangeForm, MemberRegisterForm
from mainapp.admin import CustomerOrderInline
from .models import Member

class MemberAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'created_date']
    inlines = (CustomerOrderInline,)
    add_form = MemberRegisterForm
    form = MemberChangeForm
    model = Member
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('phone_number',)}),
)
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'datetime_signed_up')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1',),
        }),
    )
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    filter_horizontal = ()

admin.site.register(Member, MemberAdmin)
