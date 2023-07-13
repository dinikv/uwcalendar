<?php
header('Content-Type: text/plain');

// Retrieve the event data from the request body
$data = json_decode(file_get_contents('php://input'), true);

// Perform any necessary processing on the event data

// Create the iCalendar file
$filename = 'apple_calendar.ics';
$calendar = new \Eluceo\iCal\Component\Calendar('My Calendar');
$event = new \Eluceo\iCal\Component\Event();
$event->setStartDate($data['begin']);
$event->setEndDate($data['end']);
$event->setSummary($data['location']);
$calendar->addComponent($event);

// Save the iCalendar file
$calendarContent = $calendar->render();
file_put_contents($filename, $calendarContent);

echo 'Calendar event created successfully.';
?>
