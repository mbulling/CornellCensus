"""
main file for cornell census
instantiates a flask app and controls route pathing
makes use of Google API (google sheet and drive), flask environment, and passing
information to html file to visualize user-submitted data. Graphs are dynamic and
reflect real-time changes to a database
"""

from flask import Flask, render_template, url_for, flash, redirect
from forms import form
import db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'



@app.route('/graphs', methods=['GET', 'POST'])
def graphs():
    """
    renders the graphs.html file
    """
    return render_template('graphs.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/forms', methods=['GET', 'POST'])
def forms():
    """
    validates form input and passes arguments to an html file
    """
    q = form()
    if q.validate_on_submit():
        college = q.cField.data
        rating = q.rField.data
        data = [college, rating]
        db.sheet.insert_row(data, db.nindex())
        c = db.getcollege()
        r = db.getrating()
        flash('data saved', 'success')
        return render_template('graphs.html', colleges=c, rating=r)

    return render_template('forms.html', form=q)

# if __name__ == '__main__':
#     app.run(debug=True)
