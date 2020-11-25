"""Route declaration."""
from flask import current_app as app
from flask import (
    url_for,
    render_template,
    redirect,
    make_response
)

from .forms import ContactForm


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template(
        'contact.html',
        form=form
    )


@app.route('/success')
def success():
    return make_response('This is success page', 200, {})


@app.route('/')
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
