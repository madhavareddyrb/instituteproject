from django.contrib import admin

# Register your models here.
from .models import CourseDetails


class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_fee', 'timings', 'start_date', 'duration', 'instructor')
admin.site.register(CourseDetails,CourseDetailsAdmin)