from django import forms
from django.core import validators # built-in django validators

def check_for_z(value): # NOTE: keyword value is necessary
    """ custom validator example """
    if value[0].lower() != 'z':
        raise forms.ValidationError('name needs to start with z')



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea) 
    

    def clean(self):
        """ special clean method for validation; think it has to be called clean() """
        all_clean_data = super().clean() # returns all cleaned data at once
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('make sure emails match')

# NOTE: this has the same structure as when we created models using class ModelName(models.model)
    
# Initial examples of form validation

# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()


#     # recall in HTML we created multi-line text inputs inside of <form></form> 
#     # using <textarea id="comment" name="comment"></textarea>; here we use the Django approach
#     text = forms.CharField(widget=forms.Textarea) 
    
#     # hidden element functioning as honey pot to catch bots
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])
    
#     ## can do this for validation but would actually use built-in Django functionality w/ validators param (see above)
#     # def clean_botcatcher(self):
#     #     botcatcher = self.cleaned_data['botcatcher']
#     #     if len(botcatcher) > 0:
#     #         raise forms.ValidationError("GOTCHA BOT!")