from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

User = get_user_model()


def send_welcome_letter(user_id):
    user = get_object_or_404(User, id=user_id)
    message = render_to_string('email_welcome.html', {
        'user': user,
    })
    subject = "Здравствуйте!"
    return user.email_user(subject, message)
