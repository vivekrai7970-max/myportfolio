from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Name',
                'class': 'form-input',
                'aria-label': 'Full name',
                'autocomplete': 'name',
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your Email',
                'class': 'form-input',
                'aria-label': 'Email address',
                'autocomplete': 'email',
            }
        ),
    )
    subject = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subject',
                'class': 'form-input',
                'aria-label': 'Message subject',
            }
        ),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your message',
                'class': 'form-textarea',
                'rows': 5,
                'aria-label': 'Your message',
            }
        ),
    )
