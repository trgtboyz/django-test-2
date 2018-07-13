from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control col-md-12 col-lg-12','placeholder':'Your Name'}))
    contact_email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control col-md-12 col-lg-12','placeholder':'Your Email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':'form-control col-md-12 col-lg-12','placeholder':'Your Message'})
    )
