from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Student

# Create your views here.
from django.template import RequestContext


def in_out(term, part):
    return term in str(part) or str(part) in term


def studenthtml(request):
    student_id = request.GET["id"][0]
    print(student_id)
    s = None
    for student in Student.objects.all():
        if str(student.student_id) == student_id:
            s = student
    return render(request, "grade_search/student.html", {"student": s})


def index(request):
    if request.POST:
        term = request.POST['term']
        print(term)
        result = []
        for student in Student.objects.all():
            if in_out(term, student.student_id) or \
                    in_out(term, student.first_name) or \
                    in_out(term, student.last_name) or \
                    in_out(term, student.address) or \
                    in_out(term, student.email) or \
                    in_out(term, student.teacher_email) or \
                    in_out(term, student.parent_email) or \
                    in_out(term, student.parent_number):
                result.append(student)
        return render(request, "grade_search/index.html", {"term": term, "result": result})
    else:
        result = []
        for student in Student.objects.all():
            result.append(student)
        return render(request, "grade_search/index.html", {"term": "", "result": result})
