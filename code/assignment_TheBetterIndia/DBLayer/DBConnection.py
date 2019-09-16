from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json


Base = declarative_base()


def make_db_uri(db_type):
        db_config_file = open('DB_config.json', 'r')
        if db_config_file.mode == 'r':
            db_config_data = json.load(db_config_file)
            if db_type == 'mysql':
                JsonObj = db_config_data['mysql']
                host = JsonObj['host']
                port = JsonObj['port']
                username = JsonObj['userName']
                password = JsonObj['password']
                dbName = JsonObj['dbName']
                db_uri = "mysql+pymysql://%s:%s@%s:%s/%s" % (username,password,host,port,dbName)
                return db_uri
            elif db_type == 'postgres':
                JsonObj = db_config_data['postgres']
                host = JsonObj['host']
                port = JsonObj['port']
                username = JsonObj['userName']
                password = JsonObj['password']
                dbName = JsonObj['dbName']
                db_uri = "postgres+psycopg2://%s:%s@%s:%s/%s" % (username,password,host,port,dbName)
                return db_uri
            else:
                raise ValueError(db_type)


def session_factory(db_type):
    if db_type == 'mysql':
        engine_mysql = create_engine(make_db_uri(db_type))
        _SessionFactory = sessionmaker(bind=engine_mysql)
        Base.metadata.create_all(engine_mysql)
        return _SessionFactory()
    elif db_type == 'postgres':
        engine_postgres = create_engine(make_db_uri(db_type))
        _SessionFactory = sessionmaker(bind=engine_postgres)
        Base.metadata.create_all(engine_postgres)
        return _SessionFactory()


#used for testing
#print(make_db_uri('postgres'))
#print(make_db_uri('mysql'))
#print(session_factory('postgres'))
#print(session_factory('mysql'))
