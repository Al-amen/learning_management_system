from rest_framework import permissions
from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserRole(BasePermission):
     message = "Only admin users are allowed to perform this action."

     def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrTeacher(BasePermission):
    """
    Allows create access to admin or teacher.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # anyone can view
        return request.user.is_authenticated and request.user.role in ['admin', 'teacher']


class IsAdminOrOwnerTeacher(BasePermission):
    """
    Admins can do anything. Teachers can update/delete only their own courses.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == 'admin':
            return True
        if request.user.role == 'teacher' and obj.instructor == request.user:
            return True
        return False
    


class IsAdminOrStudentOwner(BasePermission):
    """
    Admins can do anything. Students can only access their own enrollments.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return request.user.role == 'student' and obj.student == request.user

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'student'
    




class IsAdminOrTeacherOwner(BasePermission):
    """
    Admin can do everything. Teachers can only access their own lessons.
    Students can only view if enrolled (handled separately).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.role == 'admin':
            return True
        return request.user.role == 'teacher' and obj.instructor == request.user





class IsAdminOrTeacherMaterialOwner(BasePermission):
    """
    Admin can do everything.
    Teacher can manage materials of their courses.
    Student can only read if enrolled (handled in view).
    """

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if request.user.role == 'teacher':
            return obj.course.instructor == request.user
        if request.method in SAFE_METHODS and request.user.role == 'student':
            return obj.enrollment.student == request.user
        return False
    




class IsOwnerOrCourseInstructor(BasePermission):
    """
    - Students can create/view their own questions.
    - Teachers can update/delete if the question is on their course.
    - Admins can do anything.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == 'admin':
            return True
        if request.method in SAFE_METHODS:
            return obj.user == user or (user.role == 'teacher' and obj.course.instructor == user)
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return (
                user.role == 'admin' or
                (user.role == 'teacher' and obj.course.instructor == user) or
                (user.role == 'student' and obj.user == user)
            )
        return False
    

class IsOwnerOrCourseInstructor(BasePermission):
    """
    - Students can create/view their own questions.
    - Teachers can update/delete if the question is on their course.
    - Admins can do anything.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == 'admin':
            return True
        if request.method in SAFE_METHODS:
            return obj.user == user or (user.role == 'teacher' and obj.course.instructor == user)
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return (
                user.role == 'admin' or
                (user.role == 'teacher' and obj.course.instructor == user) or
                (user.role == 'student' and obj.user == user)
            )
        return False
