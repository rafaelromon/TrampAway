from django import forms


class MessageForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField()
