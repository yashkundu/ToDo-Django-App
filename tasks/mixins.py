from django import forms
from django.forms.utils import ErrorList

from django.shortcuts import get_object_or_404
from .models import Task
from django.core.exceptions import PermissionDenied


class FormUserNeededMixin(object):

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in to continue.'])
            return self.form_invalid(form)



class UserOwnerMixin(object):

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        if request.user != obj.user:
            raise PermissionDenied('You are not allowed to access this.')
        return super(UserOwnerMixin, self).dispatch(request, *args, **kwargs)
