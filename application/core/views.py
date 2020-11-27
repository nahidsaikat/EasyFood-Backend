"""Route declaration."""
from flask import (
    Blueprint,
    url_for,
    render_template,
    redirect,
    make_response
)

from .forms import ContactForm

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
