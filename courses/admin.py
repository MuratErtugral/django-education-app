from django.contrib import admin
from django.utils import timezone
from .models import Course, Category, Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'date', 'description', 'updated_since')
    list_filter = ('available', "date",)
    ordering = ("name",)
    search_fields = ('name', "description")
    list_editable = ("available",)
    list_per_page = 3
    date_hierarchy = "date"
    actions = ("available",)
    fieldsets = (
        (None, {
            "fields": (
                ("name", "teacher"), "available"
            ),
        }),
        ("Advanced options", {
            "fields": ("description",),
            "classes": ("collapse",),
            "description": "you can write here"
        })
    )
    def available(self, request, queryset):
        count = queryset.update(available=True)
        self.message_user(request, f"{count} lesson changed")
    
    available.short_description = 'Make available'

    def updated_since(self, course):
        difference = timezone.now() - course.date
        return difference.days 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}