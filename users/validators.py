from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

forbidden_usernames = [
    'signup',
    'login', 
    'logout', 
    'update',
    'password_change',
    'password_reset',
    'reset',
]

def forbid_username(username):
    if username in forbidden_usernames:
        raise ValidationError(
                _('Nice try, Smartypants. But your username cannot \
                    be %(username)s.'),
                params = {'username': username},
        )
