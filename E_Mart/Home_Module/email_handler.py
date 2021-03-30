from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.urls import reverse


class AppTokenGenerator(PasswordResetTokenGenerator):
   def __make_hash_value(user,timestamp):
       return text_type(user.is_active)+text_type(user.pk)+text_type(timestamp)
    
token_generator=AppTokenGenerator()

def send_link(email_subject,email_body,user,url):
    uid=urlsafe_base64_encode(force_bytes(user.pk))
    token=token_generator.make_token(user)
    link = reverse(url, kwargs={
                        'uidb64':uid, 'token': token})

    activate_url = 'http://localhost:8000'+link

    email = EmailMessage(
        email_subject,
        f'{email_body}{activate_url}', 
        'noreply@semycolon.com',
        [user.email],
    )
    email.send(fail_silently=False)
