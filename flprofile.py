"""
Login submodule for flask application
"""
from flask import Blueprint,render_template,request,flash, session, redirect, url_for

flprofile = Blueprint('flprofile', __name__, template_folder='templates', static_folder='static')


@flprofile.route('/profile/<username>')
def profile(username):
    """
    Index page for flprofile
    """
    return render_template('flprofile/profile.html', title='Твой профиль', username=username)
 