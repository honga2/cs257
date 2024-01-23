-- Find all earthquakes with a quake depth between 50 and 200 kilometers
SELECT * FROM earthquakes WHERE quakedepth BETWEEN 50 AND 200 ORDER BY mag DESC;

-- Find all earthquakes whose magnitudes were less than 2.5
SELECT * FROM earthquakes WHERE mag<2.5 ORDER BY mag ASC;

-- Find all earthquakes that occurred in Hawaii
SELECT * FROM earthquakes WHERE longitude BETWEEN -160 AND -140 AND latitude BETWEEN 0 AND 30 ORDER BY mag DESC;

