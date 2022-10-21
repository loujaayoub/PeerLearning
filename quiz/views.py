from django.shortcuts import render, redirect
# from django.db.models import Q
from account.models import Skill
from .models import Quiz, Question, Choice, Attempt, Answer
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def quizPreview(request,pk):
    quiz=Quiz.objects.get(id=pk)
    context={"quiz":quiz}
    return render(request,"quiz_preview.html",context)

@login_required(login_url="login")
def QuizPassed(request,pk):
    quiz = Quiz.objects.get(id=pk)
    attempt = Attempt.objects.create(
        quizTaker = request.user,
        quiz=quiz,
    )
    if(request.method == "POST"):
        questionIndex=0
        questionKey = "question-"+str(questionIndex)
        while questionKey in request.POST:
            questionId = request.POST.get(questionKey)
            question = Question.objects.get(id=questionId)
            answer = Answer.objects.create(
                attempt = attempt,
                question = question
            )
            choiceCount = question.choice_set.all().count()
            for choiceIndex in range(choiceCount) :
                choiceKey = str(question.id)+"-choice-"+str(choiceIndex)
                if choiceKey in request.POST:
                    choiceId = request.POST.get(choiceKey)
                    choice = Choice.objects.get(id=choiceId)
                    answer.options.add(choice)
            questionIndex+=1
            questionKey = "question-"+str(questionIndex) 
        return redirect("quiz-result",pk=attempt.id)

    context = {"quiz":quiz}   
    return render(request,"pass_quiz.html",context)

@login_required(login_url="login")
def quizResult(request,pk):
    attempt = Attempt.objects.get(id=pk)
    quiz = attempt.quiz
    score = 0
    bonus=quiz.correctAnswerMark
    penalty=quiz.wrongAnswerMark
    for answer in attempt.answer_set.all():
        rightAnswers = [choice.id for choice in answer.question.choice_set.filter(isCorrect=True)]
        givenAnswers = [choice.id for choice in answer.options.all()]
        rightAnswers.sort()
        givenAnswers.sort()
        if str(rightAnswers) == str(givenAnswers):
            score+=bonus
        else:
            score+=penalty

    attempt.score = score 
    attempt.save()
    context ={"attempt":attempt} 
    return render(request,"quiz_result.html",context) 


def quizzesPage(request):
    skills = Skill.objects.all()
    keys = [skill.skill_name for skill in skills]
    quizzes = Quiz.objects.filter(skill__skill_name__in=keys)
    return render(request, 'quizzes.html', {'quizzes': quizzes})    