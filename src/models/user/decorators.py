import functools
from typing import Callable
from flask import session, flash, redirect, url_for, request, current_app

def requires_login(f: Callable)->Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash('You need to be signed in for this page.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function
def requires_admin(f: Callable)->Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print("123")
        print(current_app.config.get('admin',''))
        if session.get('email') != current_app.config.get('admin',''):
            flash('You need to be an adminstrator to access this page.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function
