from django import forms
from django.forms import ModelForm
from .models import Images


class SignupForm(forms.Form):
    #For django authentication
    #username = forms.CharField(max_length=100, widget=forms.TextInput(
    #    attrs={
    #        "class":"form-control",
    #        "placeholder":"Username"
    #    }
    #))

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"email"
            }
        ))
    """  
    genero = forms.CharField(
        max_length=100,
        widget=forms.CharField(
            attrs={
                "class":"form-control",
                "placeholder":"genero"
            }
        ))
    """
    password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"password"
            }
        ))

    confirm_password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"confirm password"
            }
        ))
        
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class LoginForm(forms.Form):
    #For django auth
    #username = forms.CharField(max_length=100, widget=forms.TextInput(
    #    attrs={
    #        "class":"form-control",
    #        "placeholder":"Username"
    #    }
    #))
    #For custom auth
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"email"
            }
        ))
    password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"password"
            }
        ))

class ImageUploadForm(ModelForm):
    
    class Meta:
        model = Images
        fields = ('descripcion', 'imagen')
        widget = {
            'descripcion':forms.Textarea(
                attrs={
                    'rows':10,
                    'cols':15,
                    'class':'form-control',
                    'placeholder':'Escribe descripción'
                }
            )
        }