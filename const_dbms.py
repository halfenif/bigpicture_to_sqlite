import dbms


def get_dbms_type():
    return 'SQLITE'
    #return 'POSTGRESQL'

def get_conn():
    if get_dbms_type() == 'SQLITE':
        return dbms.connect.sqlite('w:/data/sqlite/db_bigpicture.db')
    elif get_dbms_type() == 'POSTGRESQL':
        return dbms.connect.postgres('bigpicture', 'bigpicture', 'bigpicture', host="192.168.0.98")
