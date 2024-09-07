#from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView
from quiz.models import *
from django.contrib.auth.models import User
from django.shortcuts import render

class UserView(View):
    def get(self, request):
        print('UserView.get()', request.POST)
        context = {
            'questions': Question.objects.count(),
            'user_count': User.objects.count(),
            'object_list': User.objects.all(),
        }
        return render(request, 'quiz/users.html', context)

    def post(self, request):
        print('UserView.post()', request.POST)
        context = {
            'questions': Question.objects.count(),
            'user_count': User.objects.count(),
            'object_list': User.objects.all(),
        }
        return render(request, 'quiz/users.html', context)

class UserTemplateView(TemplateView):
    template_name = 'quiz/users.html'

    def get_context_data(self, **kwargs):
        return {
            'questions': Question.objects.count(),
            'user_count': User.objects.count(),
            'object_list': User.objects.all(),
        }

class UserListView(ListView):
    model = User
    template_name = 'quiz/users.html'
    #object_list = User.objects.all()

    def get_queryset(self):
        return User.objects.order_by('member__country')

class UserDetailView(DetailView):
    model = User
    template_name = 'quiz/user.html'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'quiz/user_confirm_delete.html'
    success_url = '/users'

## Create Update Delete
class QuestionCreateView(CreateView):
    model = Question
    #fields = ['member', 'text']
    #fields = '__all__'
    fields = ['text']

class ChoiceCreateView(CreateView):
    model = Choice
    #fields = ['member', 'text']
    fields = '__all__'

class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = '__all__'

class ChoiceDeleteView(DeleteView):
    model = Choice

#### ---- members ----- ###
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

class QuizLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'quiz/login.html'
    #success_url = reverse_lazy('quiz_member_list')

    def get_success_url(self):
        return reverse_lazy('quiz_member_list')

class SuperUserCheck(UserPassesTestMixin):
    login_url = reverse_lazy('quiz_login')

    def test_func(self):
        print('test_func()', self.request.user.is_superuser)
        return self.request.user.is_superuser

class MemberListView(SuperUserCheck, ListView):
    paginate_by = 5
    model = Member
    template_name = 'quiz/member/list.html'

class MemberCreateView(SuperUserCheck, UpdateView):
    model = Member
    template_name = 'quiz/member/create.html'
    fields = [ 'user', 'quote', 'state', 'country' ]
    success_url = reverse_lazy('quiz_member_list')

class MemberDetailView(SuperUserCheck, DetailView):
    model = Member
    template_name = 'quiz/member/read.html'
    success_url = reverse_lazy('quiz_member_list')

class MemberUpdateView(SuperUserCheck, UpdateView):
    model = Member
    template_name = 'quiz/member/update.html'
    fields = [ 'user', 'quote', 'state', 'country' ]
    success_url = reverse_lazy('quiz_member_list')

class MemberDeleteView(SuperUserCheck, DeleteView):
    model = Member
    template_name = 'quiz/member/delete.html'
    fields = [ 'user', 'quote', 'state', 'country' ]
    success_url = reverse_lazy('quiz_member_list')
