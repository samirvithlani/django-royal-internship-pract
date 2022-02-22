from django.shortcuts import render
from django.template import context
from .models import Student


def studentData(request):

    students = Student.objects.all().values() #it will return dictonry
    #students = Student.objects.all().values_list() #it will return list of tuples

    students1 = Student.objects.filter(student_name__startswith='H').values()
    students2 = Student.objects.filter(student_name__contains='r').values()
    #lookup methods....
    #students3 = Student.objects.filter(role_id__gt=1).values() // taje integer filed like eg age...
    #students3 = Student.objects.filter(role_id__lte=1).values() // taje integer filed like eg age...
    print("filter",students2)
    print(students[0].get('id'))
    print(students[0])
    studentlist = []

    for i in students1[0].values():
        studentlist.append(i)

    print("student list",studentlist)
    
    


    # for student in students:
    #     print(list(student[0]))
        # print(student.keys(),end='')
        # print(student.items())

    context = {
        'students':studentlist
    }

    return render(request,'orm/student.html',context)
