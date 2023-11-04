from django.contrib import admin

# Register your models here.
from main_app.models import Student


# https://testdriven.io/blog/customize-django-admin/

@admin.action(description="Mark As Completed")
def mass_deactivate(model_admin, request, queryset):
    queryset.update(is_completed=True)


@admin.action(description="Mark Selected As Not Completed")
def mass_activate(model_admin, request, queryset):
    queryset.update(is_completed=False)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "is_completed")
    list_filter = ("gender",)
    search_fields = ["first_name", "last_name", "email", "phone"]
    actions = [mass_activate, mass_deactivate]

    @admin.display(description="Name")
    def full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name).capitalize()

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product Details"
        ordering = ["-first_name"]


admin.site.register(Student, StudentAdmin)
