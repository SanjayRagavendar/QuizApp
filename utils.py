from functools import wraps
from flask import jsonify, request, redirect, url_for
from flask_jwt_extended import verify_jwt_in_request, get_jwt, unset_jwt_cookies
from urllib.parse import urlparse

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request()
                claims = get_jwt()
                if claims.get('role') == 'admin':
                    return fn(*args, **kwargs)
                else:
                    return jsonify({"msg": "Course admins only!"}), 403
            except Exception as e:
                next_url = urlparse(request.url).path
                response = redirect(url_for('frontend.loginpage', next=next_url))
                unset_jwt_cookies(response)
                return response, 302        
        return decorator
    return wrapper
