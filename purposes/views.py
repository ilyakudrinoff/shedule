from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def index():
    pass


@login_required
def purposes():
    pass


@login_required
def purpose():
    pass


@login_required
def purpose_edit():
    pass


@login_required
def task():
    pass


@login_required
def task_edit():
    pass
