//QUERY SUMMARY:

//MODELS
from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.headline
//ENDMODELS


//VIEWS
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(request):
    queryset = Article.objects.all()
    context = {
        "queryset": queryset
        }
    return render(request, 'appsite/home.html', context)
//ENDWIEVS

//TEMPLATE:
 <div class="col-sm-10">

    {{instance.headline}} {{instance.description}}

{% endfor %}
			<div class='container-fluid'>
			
//ENDTEMPLATE
