from flask import Flask, request, jsonify
from ics import Calendar, Event
from datetime import datetime

app = Flask(__name__)

def create_apple_calendar_event(text):
    event = Event()

    # Parse the date and time from the text
    date_range, location = text.split(',')
    start_time, end_time = date_range.split('-')
    start_time = start_time.strip()
    end_time = end_time.strip()

    # Convert the date and time to datetime objects
    start_datetime = datetime.strptime(start_time, "%A, %B %d, %Y %I:%M %p")
    end_datetime = datetime.strptime(end_time, "%I:%M %p")

    # Set the start and end times of the event
    event.begin = start_datetime
    event.end = end_datetime

    # Set the location of the event
    event.location = location.strip()

    return event

@app.route('/create_event', methods=['POST'])
def create_event():
    event_text = request.json['eventText']
    event = create_apple_calendar_event(event_text)

    # Save the event to a file
    calendar = Calendar()
    calendar.events.add(event)
    calendar_file = 'apple_calendar.ics'
    with open(calendar_file, 'w') as f:
        f.writelines(calendar)

    return 'Calendar event created successfully.'

if __name__ == '__main__':
    app.run()
