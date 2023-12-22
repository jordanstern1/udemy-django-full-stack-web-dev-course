from django import forms


# NOTE: this has the same structure as when we created models using class ModelName(models.model)
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


    # recall in HTML we created multi-line text inputs inside of <form></form> 
    # using <textarea id="comment" name="comment"></textarea>; here we use the Django approach
    text = forms.CharField(widget=forms.Textarea) 