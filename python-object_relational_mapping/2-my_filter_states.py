#!/usr/bin/python3
'''
This module takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument exactly (case-sensitive).
'''
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306,
            user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Requête avec comparaison sensible à la casse + sécurité
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC", (state_name,))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
