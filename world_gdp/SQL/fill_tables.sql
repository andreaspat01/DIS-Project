COPY gdp
FROM 'C:\Users\Public\Documents\gdp.csv'
DELIMITER ','
CSV HEADER;

COPY gdp_growth
FROM 'C:\Users\Public\Documents\gdp_growth.csv'
DELIMITER ','
CSV HEADER;

COPY gdp_per_capita
FROM 'C:\Users\Public\Documents\gdp_per_capita.csv'
DELIMITER ','
CSV HEADER;

COPY gdp_per_capita_growth
FROM 'C:\Users\Public\Documents\gdp_per_capita_growth.csv'
DELIMITER ','
CSV HEADER;

COPY gdp_ppp
FROM 'C:\Users\Public\Documents\gdp_ppp.csv'
DELIMITER ','
CSV HEADER;

COPY gdp_ppp_per_capita
FROM 'C:\Users\Public\Documents\gdp_ppp_per_capita.csv'
DELIMITER ','
CSV HEADER;