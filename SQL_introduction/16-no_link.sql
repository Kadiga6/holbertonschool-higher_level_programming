-- Ce script liste tous les enregistrements de la table second_table où la colonne 'name' n'est pas vide
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
