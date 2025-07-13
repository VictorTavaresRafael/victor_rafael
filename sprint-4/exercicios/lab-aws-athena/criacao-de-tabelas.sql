CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes (
  ano INT,
  nome STRING,
  sexo STRING,
  total INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://bab-aws-athena-victor-rafael/';