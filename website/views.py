from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from .models import Match
from . import db
from datetime import timedelta
import os, subprocess

views = Blueprint('views', __name__)

#Index Page Directing
@views.route('/')
def home():
    return render_template("index.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/team')
def team():
    return render_template("team.html")

#User Page Directing
@views.route('/user')
@login_required
def user():
    return render_template("user.html", user=current_user)

@views.route('/user-about')
@login_required
def user_about():
    return render_template("user-about.html", user=current_user)

@views.route('/user-team')
@login_required
def user_team():
    return render_template("user-team.html", user=current_user)
    
@views.route('/user-train', methods=['GET', 'POST'])
@login_required
def train():
    output = subprocess.run(["python", "website/babyProtoss.py"], capture_output=True)

    output_lines = output.stdout.decode().split("\n")

    gameResult = [line for line in output_lines if "Result for player 2" in line][0]

    gameResult = gameResult.split()[-1]

    #gameResult = output.stdout.decode()

    new_result = Match(result=gameResult, user_id=current_user.id)
    db.session.add(new_result)
    db.session.commit()

    return render_template("user.html", user=current_user)

@views.route('/user-userPerform')
@login_required
def user_userPerform():
    matches = Match.query.filter_by(user_id=current_user.id).all()

    rows = []

    if not matches:
        no_match_row = []
        no_match_row.append("No matches found for this user.")
        rows.append(no_match_row)
    else:
        for i, match in enumerate(matches):
            num_row = []
            num_row.append("Match {}: ".format(i+1))
            rows.append(num_row)
            result_row = []
            if match.result == 'Victory':
                result_row.append("<strong>Result:</strong> Defeat")
            else:
                result_row.append("<strong>Result:</strong> Victory")
            rows.append(result_row)
            date_row = []
            date_time = match.date + timedelta(hours=8)
            date_row.append("<strong>Date and Time: </strong>{}".format(date_time))
            rows.append(date_row)
            br1_row = []
            br1_row.append("")
            rows.append(br1_row)
            br2_row = []
            br2_row.append("")
            rows.append(br2_row)
     
    return render_template("user-userPerform.html", rows=rows, user=current_user)

#Admin Page Directing
@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template("admin.html", user=current_user)

@views.route('/admin-AIPerform')
@login_required
def admin_AIPerform():
    matches = Match.query.all()

    rows = []

    if not matches:
        no_match_row = []
        no_match_row.append("No matches found.")
        rows.append(no_match_row)
    else:
        for i, match in enumerate(matches):
            num_row = []
            num_row.append("Match {}: ".format(i+1))
            rows.append(num_row)
            result_row = []
            if match.result == 'Victory':
                result_row.append("<strong>Result:</strong> Victory")
            else:
                result_row.append("<strong>Result:</strong> Defeat")
            rows.append(result_row)
            date_row = []
            date_time = match.date + timedelta(hours=8)
            date_row.append("<strong>Date and Time: </strong>{}".format(date_time))
            rows.append(date_row)
            br1_row = []
            br1_row.append("")
            rows.append(br1_row)
            br2_row = []
            br2_row.append("")
            rows.append(br2_row)

    return render_template("admin-AIPerform.html", rows=rows, user=current_user)

@views.route('/admin-updateAI',  methods=['GET', 'POST'])
@login_required
def admin_updateAI():
    if request.method == 'POST':
        file = request.files['file']

        # If a file was uploaded, save it to the desired location
        if file.filename == 'babyProtoss.py':
            file_path = os.path.join('website', 'babyProtoss.py')
            # Save the uploaded file, replacing the existing file if it exists
            file.save(file_path)
            flash('A.I Updated!', category='success')
        else:
            flash('Wrong file or no file uploaded', category='error')

    return render_template("admin-updateAI.html", user=current_user)
