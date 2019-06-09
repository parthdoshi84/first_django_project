from django.shortcuts import render

from imdb.models import Actor, Director, Producer, Movie
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from imdb.forms import ContactForm
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
import csv, io

def index(request):
    num_actors = Actor.objects.all().count()
    num_directors = Director.objects.all().count()
    
    num_producers = Producer.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_movies = Movie.objects.all().count()
    
    context = {
        'num_actors': num_actors,
        'num_producers': num_producers,
        'num_directors': num_directors,
        'num_movies': num_movies,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MovieListView(generic.ListView):
    model = Movie
    context_object_name = 'movie_list'
    def get_queryset(self):
            return self.model.objects.order_by('-rating')

class MovieDetailView(generic.DetailView):
    model = Movie
    context_object_name = "movie"
    
class ActorDetailView(generic.DetailView):
    model = Actor
    context_object_name = "actor"
    
class DirectorDetailView(generic.DetailView):
    model = Director
    context_object_name = "director"
    
class ProducerDetailView(generic.DetailView):
    model = Producer
    context_object_name = "producer"

def contact_form(request):

  

    # Create a form instance and populate it with data from the request (binding):
    form = ContactForm(request.POST)

    # Check if the form is valid:
    if form.is_valid():
     

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('message') )
    
    context = {
        'form': form
    }

    return render(request, 'imdb/contact_form.html', context)

def message(request):
    template = "success_message.html"
    context = {}
    return render(request, template, context)

def check_admin(user):
	return user.username == 'parth'

@user_passes_test(check_admin)
def actor_upload(request):
    template = "actor_upload.html"
    context={}
    if request.method == 'GET':
        return render(request, template,context)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Not a valid csv')
    
    '''readCSV = csv.reader(csv_file, delimiter=',')
    for column in readCSV:
        _,created = Actor.objects.update_or_create(
            first_name = column[0],
            last_name = column[1],
            age = column[2],
            about = column[3]
        ) '''
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter = ','):
        print(column)
        _,created = Actor.objects.update_or_create(
            first_name = column[0],
            last_name = column[1],
            age = column[2],
            about = column[3]
        )
    template = "success_message.html"
    return render(request,template, context)
    
    