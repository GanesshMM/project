from sqlalchemy import *

db_connection = "mysql+pymysql://69osz44pjrgjcwc9lwhm:pscale_pw_N5D8YDvG3jzMpgymaUZ7bXkaDcCjGF1WJ22cHkfxbtM@aws.connect.psdb.cloud/project?charset=utf8mb4"

engine = create_engine(db_connection, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as con:
  result = con.execute(text("select * from students"))
  
  columns = result.keys()
  
  result_dicts = []
  for row in result.all():
    row_dict = {}
    for column, value in zip(columns, row):
      row_dict[column] = value
    result_dicts.append(row_dict)


def load_students_from_db():
  with engine.connect() as con:
    result = con.execute(text("select * from students"))
    
    columns = result.keys()
    
    students = []
    for row in result.all():
      values = {}
      for column, value in zip(columns, row):
        values[column] = value
      students.append(values)
    return students

def load_student_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM students WHERE id={id}"))
    row = result.fetchone()
    if row is None:
      return None
    else:
      return dict(row._asdict())

