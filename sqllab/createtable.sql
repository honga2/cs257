DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  quaketime time with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  id text,
  updated time with time zone,
  place text
);
