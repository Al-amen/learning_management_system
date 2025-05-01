from django.contrib import admin

from .models import Category,Course,Enrollment,Lesson,Material,QuestionAnswer

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ('title',)
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'banner', 'price', 'duration', 'is_active', 'category_id', 'instructor_id', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ('title',)
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id', 'price', 'progress', 'is_active', 'is_completed', 'total_marks', 'is_certificate_ready', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('student_id__username', 'course_id__title')
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ('student_id',)
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video', 'course_id', 'created_at', 'updated_at')
    list_filter = ('course_id',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ('title',)
    list_editable = ('course_id',)
    date_hierarchy = 'created_at'

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file', 'course_id', 'created_at', 'updated_at')
    list_filter = ('course_id',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ('title',)
    list_editable = ('course_id',)
    date_hierarchy = 'created_at'

class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_active', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 10

    date_hierarchy = 'created_at'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)