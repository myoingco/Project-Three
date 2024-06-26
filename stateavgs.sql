CREATE TABLE StateAvgs (
    Index INTEGER PRIMARY KEY,
	Year INTEGER,
    State VARCHAR(255),
    Avg_Studio FLOAT,
    Avg_One_Bedroom FLOAT,
    Avg_Two_Bedroom FLOAT,
    Avg_Three_Bedroom FLOAT,
    Avg_Four_Bedroom FLOAT
);

INSERT INTO StateAvgs (Index,Year, State, Avg_Studio, Avg_One_Bedroom, Avg_Two_Bedroom, Avg_Three_Bedroom, Avg_Four_Bedroom)
SELECT
	MIN(Index) AS Index,
    Year,
    State,
    AVG(Studio) AS Avg_Studio,
    AVG(One_Bedroom) AS Avg_One_Bedroom,
    AVG(Two_Bedroom) AS Avg_Two_Bedroom,
    AVG(Three_Bedroom) AS Avg_Three_Bedroom,
    AVG(Four_Bedroom) AS Avg_Four_Bedroom
FROM 
    Rent
GROUP BY 
    Year, 
    State;
