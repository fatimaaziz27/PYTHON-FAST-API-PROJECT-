from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Bus(BaseModel):
    bus_id: int
    route: str
    time: str
    fare: int
    seats_available: int

class BookingRequest(BaseModel):
    name: str
    bus_id: int
    seats: int

class BookingResponse(BaseModel):
    booking_id: str
    name: str
    bus_id: int
    route: str
    time: str
    seats: int
    total_fare: int

# Data Storage
buses: dict[int, Bus] = {
    1: Bus(bus_id=1, route="North Nazimabad - Power House", time="09:00 AM", fare=500, seats_available=30),
    2: Bus(bus_id=2, route="KDA - Gulshan", time="12:00 PM", fare=700, seats_available=30),
    3: Bus(bus_id=3, route="Ayesha Manzil - Bahria", time="05:00 PM", fare=600, seats_available=30),
}

bookings: list[dict] = []
booking_id_counter: int = 1

@app.get("/buses")
def get_buses():
    return list(buses.values())

@app.post("/bookings")
def book_ticket(booking_request: BookingRequest):
    bus = buses.get(booking_request.bus_id)
    if not bus:
        return {"error": "Bus not found"}, 404
    if bus.seats_available < booking_request.seats:
        return {"error": "Not enough seats available"}, 400
    
    bus.seats_available -= booking_request.seats
    global booking_id_counter
    booking_id = f"BK{booking_id_counter}"
    booking_id_counter += 1
    booking = {
        "booking_id": booking_id,
        "name": booking_request.name,
        "bus_id": booking_request.bus_id,
        "route": bus.route,
        "time": bus.time,
        "seats": booking_request.seats,
        "total_fare": booking_request.seats * bus.fare,
    }
    bookings.append(booking)
    return booking

@app.delete("/bookings/{booking_id}")
def cancel_booking(booking_id: str):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            bus = buses.get(booking["bus_id"])
            bus.seats_available += booking["seats"]
            bookings.remove(booking)
            return {"message": "Booking cancelled successfully"}
    return {"error": "Booking not found"}, 404

@app.get("/bookings")
def get_bookings():
    return bookings

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
'''
    PROJECT MEMBERS:
    FATIMA AZIZ
    HADIYA AHMED 
    AYESHA AZIZ
    '''
