<h1 align="center"> Project 3 </h1> <br>
Utilize Python, PostgreSQL, and JavaScript to create visual representations of data.


## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Build Process](#build-process)
- [Analysis](#analysis)
- [References](#references)


## Introduction
For this project, our group chose the Data Visualization track. We decided to focus on the cumulative change in rental prices for various bedroom types from the years 2017 to 2024. The data we analyzed includes trends for studio apartments, one-bedroom, two-bedroom, three-bedroom, and four-bedroom units. By examining these trends, we aim to provide insights into how rental prices have evolved over time across different states and bedroom types.


## Getting Started
Prior to execution, you must have Visual Studio Code (VSCode) downloaded, PostgreSQL installed, and Python with the Flask library set up. 


## Build Process
1) Setup and Prerequisites:

    - Ensure you have the following installed:
        - Visual Studio Code (VSCode): For code editing.
        - PostgreSQL: For database management.
        - Python: Programming language.
        - Python Libraries: Install Flask, SQLAlchemy, Pandas, and any other necessary libraries.
        - JavaScript Libraries: Install Leaflet for mapping visualizations.

2) Database Setup:

    - Create Database: Set up a PostgreSQL database named rent_prices.
    - Create Table: Define a table in the database to store rental data.
    - Load Data: Import rental price data from a CSV file into the PostgreSQL database.
    
3) Flask API Development:

    - Setup Flask App.
    - Run Flask App: Start the Flask server to handle API requests.

4) Data Visualization:

    - Data Extraction: Use the Flask API to extract data from the PostgreSQL database.
    - Data Processing: Manipulate data using Pandas to prepare for visualization.
    
    Homepage:
    
   ![image](https://github.com/myoingco/Project-Three/assets/160566342/6cd6b7cf-2de3-4e6c-9742-56e24a879a03)

    
    Rent Price Trends By State:
    
    ![image](https://github.com/myoingco/Project-Three/assets/160566342/42d87baa-e3f5-45eb-b362-29a972464c44)

    
    Changes in Rent, Ranked By State
    
    ![image](https://github.com/myoingco/Project-Three/assets/160566342/c7a479a0-7709-469b-af74-e2c23ba26d8a)

    
    Population vs. Rental Prices
    
    ![image](https://github.com/myoingco/Project-Three/assets/160566342/7519fbaa-628d-4cae-810a-17d9c5d00645)

    
    
## Analysis
Our analysis of the cumulative change in rental prices from 2017 to 2024 across various states in the United States reveals a significant upward trend, particularly influenced by the COVID-19 pandemic. The data indicates that rental prices have surged in most states, with notable spikes in states with major cities. Factors such as increased demand for housing, reduced construction rates, and shifting population dynamics due to remote work opportunities have contributed to this rise. States like California, Rhode Island, Hawaii and Massachusetts experienced the highest increases. This highlights the need for policies to make housing more affordable and available as we recover from the pandemic.

## References
[Xpert Learning Assistant](https://bootcampspot.instructure.com/courses/5057/external_tools/313)

[Data](https://www.huduser.gov/portal/datasets/fmr.html#data_2024)
