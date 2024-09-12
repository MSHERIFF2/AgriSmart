from flask import Blueprint, request, jsonify
from app.models import FarmingTips
from app import db 
from app.auth.utils import admin_required

farming_tips = Blueprint('farming_tips', __name__)

@farming_tips.route('/farming_tips', methods=['GET'])
def get_farming_tips():
    tips = FarmingTips.query.all()
    return jsonify([tip.to_dic() for tip in tips])

@farming_tips.route('/farming_tips/<int:id>', methods=['GET'])
def get_farming_tip(id):
    tip =FarmingTips.query.get_or_404(id)
    return jsonify(tip.to_dic())

@farming_tips.route('/farming_tips', methods=['POST'])
@admin_required
def create_farming_tip():
    data = request.get_json()
    #Add data validation and admin check
    new_tip = FarmingTips(
            title=data['title'],
            conten=data['content'],
            image_url=data.get('image_url', '')
            )
    db.session.add(new_tip)
    db.session.commit()
    return jsonify(new_tip.to_dict()), 201
