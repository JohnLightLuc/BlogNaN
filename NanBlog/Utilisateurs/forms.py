# from django import forms
# from .models import *
# from django.contrib.auth.models import Group
# from django.forms import ModelMultipleChoiceField

# from django.forms.widgets import CheckboxSelectMultiple

from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.utils.translation import gettext_lazy as _
class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = models.MyUser
        fields = (
            'username',
            'email',
            'groups',
            'first_name',
            'last_name',
            'description',
            'image',
            'password1',
            'password2',
            )
        labels = {'groups': 'Type de compte', 'description': 'Votre Bio'}
        help_texts = {
            'password1': _('Some useful help text.'),
            'password2': _('Some useful help text.'),
            'username': _(''),
        }
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields =(
# 			'groups',
#             'first_name',
#             'last_name',
#             'description',
# 		)
#     def signup(self, request, user):
#         # Save your user
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.description = self.cleaned_data['description']
#         group = self.cleaned_data['groups']
#         g = Group.objects.get(name=group[0])
#         user.groups.add(g)
#         user.save()

# from allauth.account.forms import SignupForm
# class RegistrationForm(SignupForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField()
#     groups = ModelMultipleChoiceField(
#         queryset=Group.objects.order_by('name'),
#         widget=CheckboxSelectMultiple,
#     )
#     # image = models.FileField(upload_to='image/user/profile/',  blank=True, null=True)
#     description = forms.CharField(widget=forms.Textarea)


#     class Meta:
#         model = MyUser
#         labels = {'groups': 'Type de compte', 'description': 'Votre Bio'}
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.groups = self.cleaned_data['groups']
#         # user.image = self.cleaned_data['image']
#         user.description = self.cleaned_data['description']
#         user.save()
#         return user
    # def save(self, request):
    #     # group = self.cleaned_data['groups']
    #     # g = Group.objects.get(name=group[0])
    #     # print(g)
    #     # Ensure you call the parent class's save.
    #     # .save() returns a User object.
    #     user = super(RegistrationForm, self).save(request)

    #     # Add your own processing here.

    #     # You must return the original result.
    #     return user
# class EtablissementRegistrationForm(UserCreationForm):
# 	class Meta:
# 		model=EtablissementUser
# 		fields =(
# 			'username',
# 			'email',
#             'first_name',
#             'last_name',
#             'contact',
#             'avatar',
# 			'password1',
# 			'password2',
# 		)

# class EditProfileForm(UserChangeForm):

# 	class Meta:
# 		model = User
# 		fields = (
#             'username',
# 			'email',
# 			'first_name',
# 			'last_name',
# 			'contact',
#             'bio', 
# 			)
