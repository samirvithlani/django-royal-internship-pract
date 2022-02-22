from audioop import reverse
from django import views
from django.shortcuts import render
from django.template import context
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Exam
from django.views.generic import ListView

class CreateExam(CreateView):
    model = Exam
    template_name = 'exam/create.html'
    fields = ['name', 'description', 'status']
    success_url = '/'

class ExamDetail(DeleteView):
    model = Exam
    template_name = 'exam/detail.html'
    context_object_name = 'exam'

class UpdateExam(UpdateView):
    model = Exam
    template_name = 'exam/update.html'
    fields = ['name', 'description', 'status']
    context_object_name = 'exam'
    
    def get_success_url(self):
        return reverse_lazy('exam-detail', kwargs={'pk': self.object.id})   

        
class ExamList(ListView):
    model = Exam
    exams = model.objects.all().values_list('name', 'description', 'status')
    print(exams)
    template_name = 'exam/list.html'
    context_object_name = 'exams'

class DeleteExam(DeleteView):
    model = Exam
    template_name = 'exam/delete.html'
    success_url = reverse_lazy('exam_list')
