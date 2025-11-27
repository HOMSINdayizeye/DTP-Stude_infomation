from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student


# views to have all functions
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student/student_form.html', {'form': form})
    
    
def student_update(request,pk):
    student = get_object_or_404(Student, pk = pk)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student/student_form.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)   # pass the model, not request
    student.delete()
    return redirect('student_list')

