from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify, render_template,request
from flask_cors import CORS

#################################################
# Database Setup
#################################################
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/project3")

# Use inspector to check tables
inspector = inspect(engine)
tables = inspector.get_table_names()


# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)
# Print the names of the reflected tables


# Save reference to the table named 'rent' if it exists

Rent = Base.classes.rent
StateAvgs = Base.classes.stateavgs
RentDollarChange = Base.classes.rentdollarchange




#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder="")

CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/help")
def welcome():
    """List all available api routes."""
    return (
        "Available Routes:<br/>"
        "/statetrends<br/>"
        "/stateranks<br/>"
        "/pricevspop<br/>"
        "/api/scatterplot<br/>"
        "/api/rentdollarchange<br/>"
        "/api/stateavg/<state><br/>"
        "/api/alldata<br/>"
    )

@app.route("/")
def index():
    """Render the home page"""
    return render_template('template3.html')

@app.route("/pricevspop")
def pricevspop():
    """Render the scatter plot page"""
    return render_template('index3.html')

@app.route("/api/scatterplot")
def rentpopulation():
    """Retrieve rent dollar change data for all states and specified bedroom count"""
    bedroom_count = request.args.get('bedrooms', default='studio', type=str).lower()
    column_mapping = {
        'studio': 'studio',
        'one_bedroom': 'one_bedroom',
        'two_bedroom': 'two_bedroom',
        'three_bedroom': 'three_bedroom',
        'four_bedroom': 'four_bedroom'
    }

    if bedroom_count not in column_mapping:
        return jsonify({"error": "Invalid bedroom count specified"}), 400

    session = Session(engine)
    try:
        results = session.query(
            Rent.population,
            func.concat(Rent.county, func.concat(' (', Rent.state, ')')).label('county_state'),
            getattr(Rent, column_mapping[bedroom_count])
        ).all()

        coorelation = [
            {
                "population": x[0],
                "county_state": x[1],
                "rent_price": x[2]
            }
        for x in results]

        session.close()
        return jsonify(coorelation)
    except Exception as e:
        session.close()
        print(f"Error retrieving rent dollar change data: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route("/statetrends")
def statetrends():
    """Render the statetrends page"""
    return render_template('index.html')

@app.route("/stateranks")
def stateranks():
    """Render the stateranks page"""
    return render_template('index2.html')

@app.route("/api/stateavg/<state>")
def stateavg_by_state(state):
    """Retrieve average rent data by state"""
    session = Session(engine)
    try:
        avg_rent_results = session.query(
            StateAvgs.year,
            StateAvgs.state,
            StateAvgs.avg_studio,
            StateAvgs.avg_one_bedroom,
            StateAvgs.avg_two_bedroom,
            StateAvgs.avg_three_bedroom,
            StateAvgs.avg_four_bedroom
        ).filter(StateAvgs.state == state).order_by(StateAvgs.year).all()

        avg_rent = [
            {
                "year": x.year,
                "state": x.state,
                "avg_studio": x.avg_studio,
                "avg_one_bedroom": x.avg_one_bedroom,
                "avg_two_bedroom": x.avg_two_bedroom,
                "avg_three_bedroom": x.avg_three_bedroom,
                "avg_four_bedroom": x.avg_four_bedroom
            }
            for x in avg_rent_results
        ]
        session.close()
        return jsonify(avg_rent)
    except Exception as e:
        session.close()
        print(f"Error retrieving data for state {state}: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/rentdollarchange")
def rent_dollar_change():
    """Retrieve rent dollar change data for all states and specified bedroom count"""
    bedroom_count = request.args.get('bedrooms', default='studio', type=str).lower()
    column_mapping = {
        'studio': 'studio_dollar_change',
        'one_bedroom': 'one_bedroom_dollar_change',
        'two_bedroom': 'two_bedroom_dollar_change',
        'three_bedroom': 'three_bedroom_dollar_change',
        'four_bedroom': 'four_bedroom_dollar_change'
    }

    if bedroom_count not in column_mapping:
        return jsonify({"error": "Invalid bedroom count specified"}), 400

    session = Session(engine)
    try:
        results = session.query(
            RentDollarChange.state,
            getattr(RentDollarChange, column_mapping[bedroom_count])
        ).all()

        rent_changes = [
            {
                "state": x[0],
                "rent_dollar_change": x[1]
            }
        for x in results]

        session.close()
        return jsonify(rent_changes)
    except Exception as e:
        session.close()
        print(f"Error retrieving rent dollar change data: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/alldata")
def alldata():
    """List of all rent data as dictionaries"""
    session = Session(engine)
    results = [x.__dict__ for x in session.query(Rent)]
    for result in results:
        del result['_sa_instance_state']
    session.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)