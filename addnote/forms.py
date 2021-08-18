from django import forms
from addnote.models import Note

class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['subject', 'sttText', 'note_description']