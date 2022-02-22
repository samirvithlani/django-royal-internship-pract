
from django import views
from django.contrib import admin
from django.urls import include, path
from .views import CreateExam, DeleteExam, ExamDetail, ExamList, UpdateExam

urlpatterns = [
    path('create/', CreateExam.as_view(), name='create'),
    path('<int:pk>/detail',ExamDetail.as_view(), name='exam_detail'),
    path('<int:pk>/update',UpdateExam.as_view(), name='exam_update'),
    path('<int:pk>/delete',DeleteExam.as_view(), name='exam_delete'),
    path('examlist/', ExamList.as_view(), name='exam_list'),

]
