from django.db import models


from django.contrib.auth import get_user_model

User = get_user_model()

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(CommonInfo):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']

class Course(CommonInfo):
    title = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(upload_to='course_banners/',null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses',limit_choices_to={'role':'teacher'})
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)

    def __str__(self):
        return f"{self.title} - {self.instructor_id.username}"
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']

class Enrollment(CommonInfo):
    student = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_certificate_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"
    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        ordering = ['-created_at']
   

class Lesson(CommonInfo):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='lesson_videos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons',limit_choices_to={'role':'teacher'})
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['-created_at']

class Material(CommonInfo):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file_type = models.CharField(max_length=50, choices=[('pdf', 'PDF'), ('docx', 'DOCX'), ('pptx', 'PPTX')])
    file = models.FileField(upload_to='material_files/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['-created_at']

class QuestionAnswer(CommonInfo):
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'QuestionAnswer'
        verbose_name_plural = 'QuestionAnswers'
        ordering = ['-created_at']