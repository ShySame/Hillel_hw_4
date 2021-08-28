import math

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import PersonForm, Triangle
from .models import Choice, Person, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def triangle(request):
    gipot = None
    if request.method == 'POST':
        form = Triangle(request.POST)
        if form.is_valid():
            katet1 = form.cleaned_data['katet1']
            katet2 = form.cleaned_data['katet2']
            gipot = round(math.sqrt(katet1 ** 2 + katet2 ** 2), 2)
    else:
        form = Triangle()

    return render(request,
                  'polls/triangle.html',
                  {'gipot': gipot,
                   'form': form})


def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            o = Person()
            o.first_name = form.cleaned_data['first_name']
            o.last_name = form.cleaned_data['last_name']
            o.email = form.cleaned_data['email']
            o.save()
            return redirect(reverse('person'))
    else:
        form = PersonForm()

    return render(request,
                  'polls/person.html',
                  {'form': form})


def person_update(request, p_id):
    per_id = get_object_or_404(Person, pk=p_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=per_id)

        if form.is_valid():
            per_id.save()
            return redirect(reverse('person'))

    else:
        form = PersonForm(instance=per_id)

    return render(request,
                  'polls/person.html',
                  {'form': form})
