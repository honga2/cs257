DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime text,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  id text,
  updated time with time zone,
  place text
);
