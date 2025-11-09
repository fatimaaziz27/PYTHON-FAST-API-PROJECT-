## PYTHON-FAST-API-PROJECT

A simple Bus Booking API built using FastAPI.
It demonstrates how to create RESTful APIs with Python, handle requests, validate data using Pydantic, and manage basic booking logic.

Features

View available buses with route, time, fare, and seats available

Book seats for a specific bus

Cancel bookings and update seat availability

View all bookings

Simple, fast, and easy to extend

Tech Stack

Python

FastAPI

Uvicorn

Pydantic

Installation and Setup

Clone this repository:

git clone https://github.com/yourusername/PYTHON-FAST-API-PROJECT.git
cd PYTHON-FAST-API-PROJECT


Install dependencies:

pip install fastapi uvicorn pydantic


Run the FastAPI app:

uvicorn main:app --reload


Open your browser and visit:

http://127.0.0.1:8000/docs

API Endpoints
Method	Endpoint	Description
GET	/buses	Get all available buses
POST	/bookings	Book a bus ticket
GET	/bookings	Get all bookings
DELETE	/bookings/{booking_id}	Cancel a booking
Example Booking Request

POST /bookings

{
  "name": "Fatima Aziz",
  "bus_id": 1,
  "seats": 2
}


Example Response:

{
  "booking_id": "BK1",
  "name": "Fatima Aziz",
  "bus_id": 1,
  "route": "North Nazimabad - Power House",
  "time": "09:00 AM",
  "seats": 2,
  "total_fare": 1000
}

Project Members

Fatima Aziz

Hadiya Ahmed

Ayesha Aziz

Future Enhancements

Add database integration

Add user authentication

Create a frontend interface

Send booking confirmation emails

License

This project is open source under the MIT License.

Would you like me to also give you a short description line (1–2 sentences) for your GitHub project’s top section (the one that appears above the README)?
