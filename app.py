from flask import Flask, render_template, request, jsonify
import sqlite3
from database import init_db

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return render_template("index.html")


# CREATE TICKET
@app.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.get_json()

    title = data.get("title")
    description = data.get("description")

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (title, description)
        VALUES (?, ?)
    """, (title, description))

    conn.commit()
    conn.close()

    return jsonify({"message": "Ticket created successfully"}), 201


# GET ALL TICKETS
@app.route("/tickets", methods=["GET"])
def get_tickets():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()

    conn.close()

    return jsonify(tickets)


if __name__ == "__main__":
    app.run()