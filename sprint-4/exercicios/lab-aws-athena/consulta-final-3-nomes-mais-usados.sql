WITH NomesPorDecada AS (
  SELECT
    (FLOOR(ano / 10) * 10) AS decada,
    nome,
    SUM(total) AS total_decada,
    ROW_NUMBER() OVER (PARTITION BY (FLOOR(ano / 10) * 10) ORDER BY SUM(total) DESC) as ranking
  FROM
    meubanco.nomes
  WHERE
    ano >= 1950
  GROUP BY
    1, nome
)
SELECT
  decada,
  nome,
  total_decada
FROM
  NomesPorDecada
WHERE
  ranking <= 3
ORDER BY
  decada, total_decada DESC;