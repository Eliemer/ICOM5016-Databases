# Database configuration information

# Local Database (Heroku)

pg_config = {
    'user': 'zyoefirhfeajur',
    'password': 'cbc721e937823e4983756197f0bb78326e292ebf2ef214d333b9d24978b94622',
    'dbname': 'd40gme2nba4khp',
    'host': 'ec2-54-235-132-202.compute-1.amazonaws.com',
    'port': '5432'
}

dbconnect = "dbname=%s user=%s password=%s port=%s host=%s" % \
            (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['port'], pg_config['host'])

# Local Database (DataGrip)
"""
pg_config = {
    'user': 'practicalusr',
    'password': 'Machluan0212',
    'dbname': 'appdb'
}
"""
