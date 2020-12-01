"""Route declaration."""
from flask import (
    Blueprint,
    url_for,
    render_template,
    redirect,
    make_response,
    request
)
from datetime import datetime as dt

from easy_food import db
from .forms import ContactForm
from .models import User

core_bp = Blueprint(
    'core_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@core_bp.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template(
        'contact.html',
        form=form
    )


@core_bp.route('/success')
def success():
    return make_response('This is success page', 200, {})


@core_bp.route('/')
def home():
    """Landing page."""
    nav = [{'name': 'Home', 'url': 'https://example.com/1'},
           {'name': 'About', 'url': 'https://example.com/2'},
           {'name': 'Pics', 'url': 'https://example.com/3'}]
    return render_template('home.html',
                           nav=nav,
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")


@core_bp.route('/users', methods=['GET'])
def user_records():
    """Create a user via query string parameters."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(
                f'{username} ({email}) already created!'
            )
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In West Philadelphia born and raised, \
            on the playground is where I spent most of my days",
            admin=False
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_user} successfully created!")
    else:
        return render_template(
            'users.html',
            users=User.query.all(),
            title="Show Users"
        )
