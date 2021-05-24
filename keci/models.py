from django.db import models
from django.shortcuts import reverse

import datetime
import uuid

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=27)
    email = models.EmailField(max_length = 255)

    def __str__(self):
        return(self.name)

class Language(models.Model):
    languages = models.CharField(max_length=32)

    def __str__(self):
        return(self.languages)

class Stage(models.Model):
    stages = models.CharField(max_length=27)
        
    def __str__(self):
        return(self.stages)

class Branch(models.Model):
    branches = models.CharField(max_length=32)

    def __str__(self):
        return(self.branches)

class Project(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=9000, default=" ", help_text='Proje özeti...')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pub_date = models.DateField(default=datetime.datetime.now)

    language = models.ForeignKey(Language, null=True, on_delete=models.CASCADE, related_name='language')
    current_stage = models.ForeignKey(Stage, null=True, on_delete=models.CASCADE, related_name='current_stage')
    branches = models.ManyToManyField(Branch)
    authors = models.ManyToManyField(Author)

    document = models.FileField(upload_to='documents/deneme/', blank=True, null=True)
    
    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('help')
