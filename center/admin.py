from django.contrib import admin
from .models import Course, Teacher, Group, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_months', 'price')
    search_fields = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'specialization')
    search_fields = ('full_name', 'specialization')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'teacher', 'start_date', 'lesson_time')
    list_filter = ('course', 'teacher')
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'group', 'joined_date', 'is_active')
    list_filter = ('is_active', 'group')
    search_fields = ('full_name', 'phone')
