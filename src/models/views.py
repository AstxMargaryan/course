from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course

class RatingForm(forms.Form):
    rating = forms.DecimalField(label='Rating', min_value=0, max_value=5)

def first(request):
    courses = Course.objects.all()
    return render(request, 'models/first.html', {'courses': courses})

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "models/detail.html", {"course": course})

def rate_course(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            course_id = 1  # You need to specify the course ID dynamically
            try:
                course = Course.objects.get(id=course_id)
                new_rating = (course.rate * course.count + rating) / (course.count + 1)
                course.rate = new_rating
                course.count += 1
                course.save()
                return redirect('success-url')
            except Course.DoesNotExist:
                return HttpResponse('Course not found')
    else:
        form = RatingForm()
    return render(request, 'rate_course.html', {'form': form})



