from flask import render_template, Blueprint, flash, session, redirect, url_for, request
from project.users.forms import LoginForm

bp = Blueprint('users', __name__)


@bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():  # request is POST
        user = form.username.data
        flash(f'Welcome {user}', 'info')
        session['username'] = user

        return redirect(url_for('classifier.index'))

    # GET
    return render_template('simple_form.html', form=form, url='users.login')


@bp.route('/forget', methods=['POST'])
def expire():
    flash(f"{session['username']}, your session has expired.", 'info')
    del session['username']
    return redirect(url_for('users.login'))


