from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.utils import timezone

from ratings.models import Question, Subject
from ratings.forms import QuestionForm
from ipware.ip import get_ip
from IPython import embed

import logging
import random

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
  subject = Subject()
  ip = get_ip(request)
  if ip is not None:
    subject.ip_address = ip
  subject.save()
  request.session['subject_id'] = subject.id

  # Plan the test run (hardcoded to Experiment 1 for now)
  images = [i for i in xrange(1, 51)]
  random.shuffle(images)

  request.session['total_images'] = len(images)
  
  first_image = images[0]
  images = images[1:]

  request.session['image_order'] = images

  return render(request, 'ratings/index.html', {
    'first_image': first_image,
    'experiment_empty': False,
    'total_images': request.session['total_images'],
  })

# This provides the basic survey form
def question(request, image_id):
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    # Check whether it's valid
    if form.is_valid():
      # SAVE IT
      question = Question()
      question.subject = Subject.objects.get(pk=request.session['subject_id'])
      question.image = form.cleaned_data['image']
      question.name = form.cleaned_data['name']
      question.recognizability = int(form.cleaned_data['recognizability'])
      question.familiarity = int(form.cleaned_data['familiarity'])
      question.pleasantness = int(form.cleaned_data['pleasantness'])
      question.complexity = int(form.cleaned_data['complexity'])
      question.memorability = int(form.cleaned_data['memorability'])

      question.save()

      # If this is the last question, direct the user to the THANKS page
      finished = False
      next_image = False
      if len(request.session['image_order']) > 0:
        next_image = request.session['image_order'][0]
        request.session['image_order'] = request.session['image_order'][1:]
      else:
        finished = True
      if finished:
        return HttpResponseRedirect('/thanks/')
      else:
        return HttpResponseRedirect('/question/' + str(next_image))
    else:
      # THERE ARE FORM ERRORS OMG WHAT DO WE DO
      return render(request, 'ratings/question.html', {
        'form': form,
        'image_path': image_id + '.jpg',
        'image_id': image_id,
        'images_left': len(request.session['image_order']), 
        'subject_id': request.session['subject_id'],
        'images': request.session['image_order']
        })
  else:
    image = image_id
    form = QuestionForm()
    return render(request, 'ratings/question.html', {
      'form': form,
      'image_path': str(image) + '.jpg',
      'image_id': image,
      'images_left': len(request.session['image_order']), 
      'subject_id': request.session['subject_id'],
      'images': request.session['image_order'],
      })

def thanks(request):
  return render(request, 'ratings/thanks.html')