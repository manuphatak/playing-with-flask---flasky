#!/usr/bin/env python
# coding=utf-8

from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, login_required, logout_user

from .. import db
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('You have been logged in. Welcome back %s!' % user.username)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        flash('Welcome %s!  You can now login.' % user.username)
        return redirect(url_for('auth.login'))

    return render_template('auth/registration.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
