-- SHOWS ALL THE CITIES OF CALIFORNIA THAT CAN BE FOUND IN THE DATABASE HBTN_0D_USA
SELECT id, name FROM hbtn_0d_usa.cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
