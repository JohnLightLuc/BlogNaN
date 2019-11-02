from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import Group
from . import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.conf import settings


def inscription(request):
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            group=form.cleaned_data.get("groups")
            print(group[0], email)
            user = form.save()
            user.is_active = False
            user.save()
            users = models.MyUser.objects.filter(email=email)
            choice=group[0]
            groupe = Group.objects.get( name = choice )
            for item in users:
                print(item.id)
                item.groups.add(groupe)
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            mail = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
            mail.send()
            return redirect('sign_send_verif')
    else:
        form= forms.RegistrationForm()
    return render(request, 'account/signup.html', {
        'form':form
    })

def signup_sendmail(request):
    return render(request, 'account/signup_confirm.html')
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]
            # )
    #         # email.send()
    #         return HttpResponse('Please confirm your email address to complete the registration')
    # else:
    #     form = SignupForm()
    # return render(request, 'signup.html', {'form': form})
def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = models.MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, models.MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        print("iudisd")
        return render(request, 'account/verif_ok.html')
    else:
        return render(request, 'account/invalid_link.html')