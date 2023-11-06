from django.contrib import admin

from .models import Department, Employee, Project, TimeEntry


admin.site.register(Department)


#admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    class TimeEntryInline(admin.TabularInline):
        model = TimeEntry

    inlines = [TimeEntryInline]


#admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    class TimeEntryInline(admin.TabularInline):
        model = TimeEntry

    inlines = [TimeEntryInline]


admin.site.register(TimeEntry)
