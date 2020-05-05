from django import forms

class ContactForm(forms.Form):

    fullName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Full Name"
            }
        )
    )
    
    email    = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Email"
            }
        )
    )
    content  = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Type your Message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if not "gmail" in email:
            raise forms.ValidationError("Must be Associated with Gmail")

        return email
    