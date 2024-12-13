from flask import Flask, jsonify, request, abort
import uuid

# Initialize the Flask app
app = Flask(__name__)

# In-memory "database" for staff
staff = []

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the BestBuy Staff-Service API! Use /staff to manage staff data.", 200

# Health check route (GET)
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Route to retrieve all staff members (GET request)
@app.route('/staff', methods=['GET'])
def get_staff():
    return jsonify(staff), 200

# Route to retrieve a single staff member by their ID (GET request)
@app.route('/staff/<string:staff_id>', methods=['GET'])
def get_staff_member(staff_id):
    member = next((s for s in staff if s['id'] == staff_id), None)
    if member is None:
        abort(404)  # Staff member not found
    return jsonify(member), 200

# Route to create a new staff member (POST request)
@app.route('/staff', methods=['POST'])
def create_staff():
    if not request.json or 'name' not in request.json:
        abort(400)  # Bad request
    new_member = {
        "id": str(uuid.uuid4()),  # Generate a unique ID
        "name": request.json['name'],
        "position": request.json.get('position', ''),
        "department": request.json.get('department', ''),
        "email": request.json.get('email', ''),
        "phone": request.json.get('phone', '')
    }
    staff.append(new_member)
    return jsonify(new_member), 201  # Created

# Route to update an existing staff member (PUT request)
@app.route('/staff/<string:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    member = next((s for s in staff if s['id'] == staff_id), None)
    if member is None:
        abort(404)  # Staff member not found
    if not request.json:
        abort(400)  # Bad request
    # Update the staff member's attributes
    member['name'] = request.json.get('name', member['name'])
    member['position'] = request.json.get('position', member['position'])
    member['department'] = request.json.get('department', member['department'])
    member['email'] = request.json.get('email', member['email'])
    member['phone'] = request.json.get('phone', member['phone'])
    return jsonify(member), 200  # OK

# Route to delete a staff member (DELETE request)
@app.route('/staff/<string:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    global staff
    staff = [s for s in staff if s['id'] != staff_id]
    return '', 204  # No Content

# Entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
