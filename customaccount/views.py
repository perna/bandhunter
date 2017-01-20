import account.forms
import account.views
import customaccount.forms
import uuid


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):
    form_class = customaccount.forms.SignupForm

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = uuid.uuid4()
        return username
