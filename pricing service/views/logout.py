from flask import Blueprint, url_for, session, redirect
logout_blueprint = Blueprint("logout", __name__)
@logout_blueprint.route('/')
def logout():
    session['email']=None
    return redirect(url_for('users.login_user'))
