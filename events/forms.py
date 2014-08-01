from django import forms

from .models import Event


class EventAdminForm(forms.ModelForm):
    """
    Form class for editing events in the admin interface.
    """
    location = forms.CharField(label="Address", required=False, max_length=200,
            widget=forms.TextInput(attrs={'class': 'vTextField'}))
    description_markdown = forms.CharField(label="Description",
            widget=forms.Textarea(attrs={'class': 'vLargeTextField'}),
            help_text="Use <a href='http://daringfireball.net/projects/markdown/basics'>Markdown formatting</a>")

    class Meta:
        model = Event
        exclude = ('description',)
