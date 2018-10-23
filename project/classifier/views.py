from flask import render_template, Blueprint, session, redirect, url_for, flash
from project.classifier.forms import ClassifierForm

bp = Blueprint('classifier', __name__,
               url_prefix='/classifier')


@bp.route('/')
def index():
    if 'username' not in session:
        flash('Hi, please tell us who you are!', 'info')
        return redirect(url_for('users.login'))
    form = ClassifierForm()
    return render_template('simple_form.html', form=form, url='classifier.index')


@bp.route('/result', methods=['POST'])
def result():
    pass


@bp.route('/show/<flower>')
def show(flower):
    # show the flower image
    pass
