-- Ce script sélectionne les enregistrements de la table second_table avec un score >= 10.
-- Les résultats sont triés par score, du plus élevé au plus bas.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
