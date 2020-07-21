from django import forms


class ContactForm(forms.Form):
    """ Create form for contact page """

    subject = forms.CharField(
        required=True,
        label='Subject',
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
    sender = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
