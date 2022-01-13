"""
main file for cornell census
instantiates a flask app and controls route pathing
makes use of Google API (google sheet and drive), flask environment, and passing
information to html file to visualize user-submitted data. Graphs are dynamic and
reflect real-time changes to a database
"""

from flask import Flask, render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, login_required, logout_user, current_user
from .forms import form
from .models import User
from . import db

cornellcensus = Blueprint('cornellcensus', __name__)

@cornellcensus.route('/graphs', methods=['GET', 'POST'])
def graphs():
    """
    renders the graphs.html file
    """
    labels = ["Engineering", "CALS", "CAS"]
    values = [600, 50, 200, 550, 320]
    return render_template('graphs.html', labels=labels, values=values)

@cornellcensus.route('/', methods=['GET', 'POST'])
def forms():
    """
    validates form input and passes arguments to an html file
    """
    q = form()
    if q.validate_on_submit():
        school = q.cField.data
        school = "College of Engineering"
        rating = q.rField.data
        year = q.yField.data
        major = q.mField.data
        rating = 299

        user = User.query.filter_by(school=school).first()

        new_user = User(school=school, rating=rating)
        db.session.add(new_user)
        db.session.commit()
       
        flash('data saved', 'success')
        labels = ["Engineering", "CALS", "CAS"]
        values = [600, 50, 200, 550, 320]
        return render_template('graphs.html', user=current_user, labels=labels, values=values, rating=rating)

    return render_template('forms.html', form=q)


