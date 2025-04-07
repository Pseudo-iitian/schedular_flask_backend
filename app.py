from flask import Flask, jsonify, request  # Added 'request' here
from datetime import datetime, timedelta
import pywhatkit as pwt
from flask_cors import CORS  # ✅ Import CORS
import time

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes


# Your provided data
schedule_data = {
    "8": {
        "assignments": [
            "Vikas Prabhu",
            "Aish Prabhu",
            "Bikas Prabhu",
            "Aditya Prabhu",
            "Abhishek Verma Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "9": {
        "assignments": [
            "Aish Prabhu",
            "Bikas Prabhu",
            "Aditya Prabhu",
            "Abhishek Verma Prabhu",
            "Kartik Sadh Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "10": {
        "assignments": [
            "Bikas Prabhu",
            "Aditya Prabhu",
            "Abhishek Verma Prabhu",
            "Kartik Sadh Prabhu",
            "Ashish Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "11": {
        "assignments": [
            "Aditya Prabhu",
            "Abhishek Verma Prabhu",
            "Kartik Sadh Prabhu",
            "Ashish Prabhu",
            "Abhishek Batabyal Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "12": {
        "assignments": [
            "Abhishek Verma Prabhu",
            "Kartik Sadh Prabhu",
            "Ashish Prabhu",
            "Abhishek Batabyal Prabhu",
            "Vikas Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "13": {
        "assignments": [
            "Kartik Sadh Prabhu",
            "Ashish Prabhu",
            "Abhishek Batabyal Prabhu",
            "Vikas Prabhu",
            "Aish Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "14": {
        "assignments": [
            "Ashish Prabhu",
            "Abhishek Batabyal Prabhu",
            "Vikas Prabhu",
            "Aish Prabhu",
            "Bikas Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    },
    "15": {
        "assignments": [
            "Abhishek Batabyal Prabhu",
            "Vikas Prabhu",
            "Aish Prabhu",
            "Bikas Prabhu",
            "Aditya Prabhu"
        ],
        "programs": [
            "Deity worship",
            "Mangla arti",
            "Narasimha arti",
            "Tulsi arti",
            "Shikshashtakam"
        ]
    }
}


@app.route('/api/send_tomorrow_schedule', methods=['POST'])
def send_tomorrow_schedule():

    # Get day from request body
    data = request.get_json()
    
    if not data or 'day' not in data:
        return jsonify({
            "status": "error",
            "message": "Please provide 'day' in request body (1-31)"
        }), 400
    
    day = data['day']
    
    # Validate day (1-31)
    try:
        day = int(day)
        if day < 1 or day > 31:
            raise ValueError
    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid day. Please enter a number between 1-31"
        }), 400
    
    # Calculate schedule key
    val = day % 8
    res = 8 + val
    schedule_key = str(res)
    
    # Get the schedule
    schedule = schedule_data.get(schedule_key, schedule_data["8"])
    
    # Format the response
    assignments = schedule["assignments"]
    programs = schedule["programs"]
    
    lines = []
    for program, assignee in zip(programs, assignments):
        lines.append(f"-{program} - {assignee}")
    
    formatted_date = f"{day} {datetime.now().strftime('%b %Y')}"  # Shows "31 Apr 2025" format
    message = f"✨Hare Krishna Schedule for ({formatted_date}) 🌞\n\n"
    message += "\n".join(lines)
    message += "\n\nYour Servant"
    
    return jsonify({
        "status": "success",
        "day": day,
        "schedule_key": schedule_key,
        "schedule": message
    })

if __name__ == '__main__':
    app.run(debug=True)
