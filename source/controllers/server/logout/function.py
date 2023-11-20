from flask import redirect, url_for
from flask_login import logout_user


def _process_logout():
    logout_user()
    return redirect(url_for('system.home.home'))
