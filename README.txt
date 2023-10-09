Project Name: RAM Usage Monitoring and API Interface

Description: This project monitors RAM usage and provides an API interface. Built with Python, FastAPI, psutil, SQLAlchemy, and bcrypt for password hashing.

Prerequisites:

Python 3.6 or higher
Virtual environment recommended
Usage:

Clone the repository and install dependencies.
Run RAM Usage Monitor: python main.py
Access API Interface: uvicorn api_interface:app --reload
Endpoints: http://localhost:8000/docs
Create Users: python user_creator.py
API Endpoints:

GET /login: User authentication, provides a token.
GET /get_ram_data/: Retrieve RAM usage data, supports limit parameter.