from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from app.models import FarmingTips
from app import db 
from app.auth.utils import admin_required

farming_tips = Blueprint('farming_tips', __name__)

# Route to fetch all farming tips and render the farming tips page
@farming_tips.route('/farming_tips', methods=['GET'])
def get_farming_tips():
    tips = FarmingTips.query.all()
    return render_template('farming_tips.html', tips=tips)  # Render the template with farming tips

# Route to fetch a specific farming tip and render a detailed view
@farming_tips.route('/farming_tips/<int:id>', methods=['GET'])
def get_farming_tip(id):
    tip = FarmingTip.query.get_or_404(id)
    return render_template('farming_tip_detail.html', tip=tip)  # Render a detailed template

# Route to create a new farming tip, accessible only to admins
@farming_tips.route('/farming_tips/create', methods=['GET', 'POST'])
@admin_required
def create_farming_tip():
    if request.method == 'POST':
        data = request.form  # Using form data from a submitted HTML form
        # Add data validation here if needed
        new_tip = FarmingTips(
            title=data['title'],
            content=data['content'],
            image_url=data.get('image_url', '')
        )
        db.session.add(new_tip)
        db.session.commit()
        return redirect(url_for('farming_tips.get_farming_tips'))  # Redirect after creating a new tip

    # Render the form to create a new farming tip
    return render_template('create_farming_tip.html')
