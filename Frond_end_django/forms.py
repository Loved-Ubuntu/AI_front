from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

class settings_shape_form(forms.Form):
    scale = forms.CharField()
    blur = forms.CharField()
    edges = forms.CharField()
    grayscale = forms.CharField()
    threshold = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_methode = 'POST'
        self.fields['blur'].required = False
        self.fields['edges'].required = False
        self.fields['grayscale'].required = False
        self.fields['threshold'].required = False


        self.helper.layout = Layout(
            'scale',
            'blur',
            'edges',
            'grayscale',
            'threshold',
            Submit('submit', 'Change', css_class='ui blue button')
        )