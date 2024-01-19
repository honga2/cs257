DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime timestamp with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  id text,
  updated text,
  place text
);
