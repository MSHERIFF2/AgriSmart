from functools import wraps
from flask import session, jsonify
from app.models import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"message": "Authentication required"}), 401
        user = User.query.get(user_id)
        if not user or not uer.is_admin:
            return jsonify({"message": "Admin access required"}), 403
        return f(*args, **kwargs)
    return decorated_function
