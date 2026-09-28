from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Teacher, Group, Student
from .forms import CourseForm, StudentForm


def home_view(request):
    courses_count = Course.objects.count()
    groups_count = Group.objects.count()
    teachers_count = Teacher.objects.count()
    active_students_count = Student.objects.filter(is_active=True).count()

    context = {
        'courses_count': courses_count,
        'groups_count': groups_count,
        'teachers_count': teachers_count,
        'active_students_count': active_students_count,
    }
    return render(request, 'home.html', context)


def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_create_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})


def group_list_view(request):
    groups = Group.objects.select_related('course', 'teacher').all()
    return render(request, 'groups/group_list.html', {'groups': groups})


def student_list_view(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.select_related('group').all()
    if query:
        students = students.filter(full_name__icontains=query)

    return render(request, 'students/student_list.html', {'students': students, 'query': query})


def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'O‘quvchi qo‘shish'})


def student_update_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'title': 'O‘quvchini tahrirlash'})


def student_delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
