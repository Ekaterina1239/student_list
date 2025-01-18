from django.shortcuts import render

from app.models import Student


# Create your views here.
def student_list_view(request):
    context = {'students': Student.objects.all()}
    return render(request, 'app/student_list.html', context)


def student_view(request):
    return render(request, 'app/student.html')
