from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator, Page, EmptyPage
from django.http.response import Http404
from forms import AnswerForm, AskForm
from django.views.decorators.http import require_POST

def paginate(qs, page=1, limit=10):
    try:
        limit = int(limit)
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(page)
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    questions = Question.objects.sort_by_id().all()
    page = paginate(questions, page)
    paginator = page.paginator
    paginator.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
        'title': 'New questions',
        })


def popular_questions(request):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    questions = Question.objects.sort_by_rating().all()
    page = paginate(questions, page)
    paginator = page.paginator
    paginator.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
        'title': 'Popular questions',
        })


def question(request, id):
    try:
        id = int(id)
    except:
        raise Http404
    try:
        q = Question.objects.filter(pk=id)[0]
    except Question.DoesNotExist:
        raise Http404
    try:
        answers = q.answer_set.all()
        print answers
    except:
        answers = None
    form = AnswerForm(initial={'question': q.id})
    return render(request, 'question.html', {
        'question': q,
        'answers': answers,
        'title': 'Question',
        'form': form,
    })


def add_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'add_question.html', {
        'form': form,
    })


@require_POST
def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(answer.get_url())
    return HttpResponseRedirect(request.META.HTTP_REFERER)



