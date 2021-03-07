
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _




class pass_validator(object):
    def validate(self, password, user=None):
        if not re.findall('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password):
            raise ValidationError(
                _("Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters."),
                code='password_no_number',
            )

    def get_help_text(self):
        return (
            "Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters."
        )



