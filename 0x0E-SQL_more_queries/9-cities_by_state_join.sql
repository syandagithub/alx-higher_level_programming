-- SHOWS ALL CITIES IN THE DATABASE HBTN_0D_USA.
SELECT cities.id, cities.name, states.name FROM cities 
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
