from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField

class Suggestion(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Status')
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'statuses'

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    sid = models.ForeignKey(Suggestion)

    def __unicode__(self):
        return self.comment[:50]

class SuggestionForm(ModelForm):
	class Meta:
		model = Suggestion
		fields = ['title', 'description', 'category']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']

	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['comment'].widget.attrs['class'] = "form-control"
		self.fields['comment'].widget.attrs['rows'] = "2"

class StatusForm(ModelForm):
	status = ModelChoiceField(queryset=Status.objects.all(), empty_label=None)
	
	def __init__(self, *args, **kwargs):
		super(StatusForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Status
		fields = ['status']
