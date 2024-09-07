from django.urls import path
from django.contrib.auth.views import LogoutView
from quiz.views import *
from quiz.classview import *

urlpatterns = [
    path('', home, name='quiz-home'),
    #path('users/', users, name='quiz-users'),
    path('users/', UserView.as_view(), name='quiz-users'),
    path('users2/', UserTemplateView.as_view(), name='quiz-users-2'),
    path('users3/', UserListView.as_view(), name='quiz-users-3'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='quiz-user-detail'),
    #path('username/<slug:slug>/', UserDetailView.as_view(), name='quiz-user-slug'),
    path('create/', create),
    path('json/', json),
    path('pdf/', pdf),
    path('bg/', bg),
    path('blurbg/', blurbg),

    path('question/create/', QuestionCreateView.as_view(), name='quiz-question-create'),

    path('choice/create/', ChoiceCreateView.as_view(), name='quiz-choice-create'),
    path('choice/update/<int:pk>/', ChoiceUpdateView.as_view(), name='quiz-choice-update'),
    path('choice/delete/<int:pk>/', ChoiceDeleteView.as_view(), name='quiz-choice-delete'),

    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='quiz-user-delete'),

    path('member/list',             MemberListView.as_view(),   name='quiz_member_list'),
    path('member/create/',          MemberCreateView.as_view(), name='quiz_member_create'),
    path('member/read/<int:pk>/',   MemberDetailView.as_view(), name='quiz_member_read'),
    path('member/update/<int:pk>/', MemberUpdateView.as_view(), name='quiz_member_update'),
    path('member/delete/<int:pk>/', MemberDeleteView.as_view(), name='quiz_member_delete'),

    path('quiz/login/', QuizLogin.as_view(), name='quiz_login'),
    path('quiz/logout/', LogoutView.as_view(next_page='quiz-home'), name='quiz_logout'),
]

