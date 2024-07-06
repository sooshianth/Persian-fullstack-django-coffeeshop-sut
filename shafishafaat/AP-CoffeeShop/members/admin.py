from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mainapp.admin import CustomerOrderInline
from .models import Member


class MemberCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ('username', 'first_name', 'last_name')

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ('username', 'first_name', 'last_name', 'is_active', 'is_staff',)


class MemberAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'created_date']
    inlines = (CustomerOrderInline,)
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ()}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Member, MemberAdmin)
