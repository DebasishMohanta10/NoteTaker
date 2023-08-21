from django import forms
from .models import Note
class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields= ["short_note","content"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control my-3"
        self.fields['short_note'].label= "Title"
        self.fields['content'].widget.attrs["rows"] = 3
        self.fields['short_note'].widget.attrs['placeholder']= "Title of the Note (Optional)"
        self.fields['content'].widget.attrs['placeholder']= "Write the Content Note (500 words)"