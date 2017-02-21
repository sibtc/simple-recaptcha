from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        required=True,
        max_length=1000
    )

    class Meta:
        model = Comment
        fields = ('text', )