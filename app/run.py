import uvicorn
from fastapi import FastAPI # need python-multipart
import views, psycopg2
import logging, os
from database.models import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Session
from database.config import config
import psycopg2

app = FastAPI(title="Challenge", version="1.6")

app.include_router(views.router)

#PostgreSQL flavor 
#Change your DB to test
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:H0useMD-I@localhost:5432/postgres" 

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# def connect():

#     conn = None

#     try:
#         print('Connecting to postgresql database')
#         params = config()
#         conn = psycopg2.connect(**params)

#         cursor = conn.cursor()

#         print('Postgresql database version:')
#         cursor.execute('SELECT VERSION()')

#         db_version = cursor.fetchone()
#         print(db_version)

#         # cursor.close()

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('Database connection closed')

def init(db: Session) -> None:
    db = Session_local

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname + '\data', 'business_symptom_data.csv')
    # db.execute(f"copy table_name FROM '{business_symptom_data.csv}' WITH CSV;", execution_options=None)

    conn = None

    try:
        print('Connecting to postgresql database')
        params = config()
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        print('Postgresql database version:')
        cursor.execute('SELECT VERSION()')

        db_version = cursor.fetchone()
        print(db_version)

        # cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    with open(filename, 'r') as f:    
        cursor = conn.cursor()
        cmd = 'COPY (col1, col2, col3, col4, col5) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        cursor.copy_expert(cmd, f)
        conn.commit()

def main() -> None:
    logger.info("Creating initial data")
    init(Base)
    logger.info("Initial data created")

if __name__ == '__main__':
    main()
    uvicorn.run(app, host='127.0.0.1', port=8013, log_level="debug")
