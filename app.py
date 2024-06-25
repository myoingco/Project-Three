
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

from flask import Flask, jsonify, render_template
from flask_cors import CORS


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///ball.sqlite")

# HERE IS HOW TO USE POSTGRES
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/project3")
# my example
#engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/practice")meichelyoingco

# Use inspector to check tables
inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)


# # reflect an existing database into a new model
Base = automap_base()

# # reflect the tables
Base.prepare(autoload_with=engine)
# Print the names of the reflected tables
print("Reflected tables:", Base.classes.keys())

# Save reference to the table named 'rent' if it exists
if 'rent' in Base.classes:
    Rent = Base.classes.rent
    # Get the column names of the 'rent' table
    rent_columns = Rent.__table__.columns.keys()
    print("Columns in 'rent' table:", rent_columns)
else:
    print("Table 'rent' not found.")

# # Save reference to the table
# Rents = Base.classes.rent
# rent_columns = Base.classes.rent.__table__.columns.keys()
# print(rent_columns)
# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__, template_folder="")

# CORS(app)


# #################################################
# # Flask Routes
# #################################################

# @app.route("/help")
# def welcome():
#     """List all available api routes."""
#     return (
#         "Available Routes:<br/>"
#         "/api/player/<player_name><br/>"
#         "/api/bypts/<pts><br/>"
#         "/api/allplayers<br/>"
#     )

# @app.route("/")
# def index():
#     """Render the home page"""
#     return render_template('template.html')

# @app.route("/api/player/<player_name>")
# def by_player(player_name):
#     """ search by player """
#     session = Session(engine)

#     # Query all player
#     query_results = session.query(Players).filter(Players.Player == player_name)
#     results = [{"id": x.id, "player": x.Player} for x in query_results]

#     print(results)
#     session.close()
#     return jsonify(results)


# @app.route("/api/bypts/<pts>")
# def by_pts(pts):
#     """ search by pts"""
#     session = Session(engine)
#     # THIS CODE ISN'T FINISHED
#     # POINTS ARE TEXT! NOT INTEGERS
#     # Query all passengers
#     query_results = session.query(Players).filter(Players.PTS > pts)
#     results = [{"id": x.id, "player": x.Player, "pts": x.PTS} for x in query_results]

#     print(results)
#     session.close()
#     return jsonify(results)


# @app.route("/api/allplayers")
# def allplayers():
#     """ list of all players as dictionaries """
#     session = Session(engine)
#     # get all columns
#     results = [x.__dict__ for x in session.query(Players)]
#     for result in results:
#         del result['_sa_instance_state']
#     session.close()

#     return jsonify(results)

# if __name__ == '__main__':
#     app.run(debug=True)
