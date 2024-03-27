# from django import forms
# from captcha.fields import ReCaptchaField
from django_recaptcha.fields import ReCaptchaField
from allauth.account.forms import SignupForm 

class CustomSignupForm(SignupForm):
    captcha = ReCaptchaField()

    # def save(self, request):
    #     user = super(CustomSignupForm, self).save(request)
    #     return user
    
# from django import forms
# from captcha.fields import ReCaptchaField
# from django_recaptcha.fields import ReCaptchaField

# class AllauthSignupForm(forms.Form):
 
    # captcha = ReCaptchaField(widget=ReCaptchaWidget())
    # captcha = ReCaptchaField()
 
    # def signup(self, request, user):
    #     """ Required, or else it throws deprecation warnings """
    #     pass