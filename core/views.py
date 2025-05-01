from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

from rest_framework import generics


User = get_user_model()
from core.models import(
    Category,
    Course,
    Enrollment,
    Lesson,
    Material,
    QuestionAnswer
) 

from api.serializers import (
    #UserSerializer,
    CategorySerializer,
    CourseSerializer,
    EnrollmentSerializer,
    LessonSerializer,
    MaterialSerializer,
    QuestionAnswerSerializer
)
from .custom_permission import (
    IsAdminUserRole,
    IsAdminOrTeacher,
    IsAdminOrOwnerTeacher,
    IsAdminOrStudentOwner,
    IsAdminOrTeacherOwner,
    IsAdminOrTeacherMaterialOwner,
    IsOwnerOrCourseInstructor,

)

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            if not self.request.user.is_authenticated:
                raise PermissionDenied("Authentication required to create a category.")
            if self.request.user.role != 'admin':
                raise PermissionDenied("Only admin users can create categories.")
        return [AllowAny]
    

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_authenticated:
                raise PermissionDenied("Authentication required to modify a category.")
            if self.request.user.role != 'admin':
                raise PermissionDenied("Only admin users can update or delete categories.")
        return [AllowAny]
        



class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrTeacher]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_id', 'instructor_id'] 

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrOwnerTeacher]
    
    


class EnrollmentListCreateView(generics.ListCreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Enrollment.objects.all()
        return Enrollment.objects.filter(student=user)

    def perform_create(self, serializer):
        course = serializer.validated_data['course']
        serializer.save(student=self.request.user, price=course.price)

class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStudentOwner]




class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Lesson.objects.all()
        elif user.role == 'teacher':
            return Lesson.objects.filter(instructor=user)
        elif user.role == 'student':
            enrolled_courses = Enrollment.objects.filter(student=user).values_list('course_id', flat=True)
            return Lesson.objects.filter(course_id__in=enrolled_courses)
        return Lesson.objects.none()

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTeacherOwner]



class MaterialListCreateView(generics.ListCreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Material.objects.all()
        elif user.role == 'teacher':
            return Material.objects.filter(course__instructor=user)
        elif user.role == 'student':
            enrollments = Enrollment.objects.filter(student=user).values_list('id', flat=True)
            return Material.objects.filter(enrollment_id__in=enrollments)
        return Material.objects.none()

    def perform_create(self, serializer):
        # Optional: auto-link enrollment for teacher/admin based on course+student if known
        serializer.save()

class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTeacherMaterialOwner]





class QuestionAnswerListCreateView(generics.ListCreateAPIView):
    serializer_class = QuestionAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return QuestionAnswer.objects.all()
        elif user.role == 'teacher':
            return QuestionAnswer.objects.filter(course__instructor=user)
        elif user.role == 'student':
            return QuestionAnswer.objects.filter(user=user)
        return QuestionAnswer.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QuestionAnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrCourseInstructor]