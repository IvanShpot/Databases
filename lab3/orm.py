from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:Pr0gr3s'
                       '@localhost:5432/School', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def recreate():
    Base.matadata.drop_all(engine)
    Base.matadata.create_all(engine)

class subjects(Base):
    __tablename__ = 'subjects'
    subjects_id = Column(Integer, primary_key=True)
    name = Column(String)
    sched = relationship("schedule", order_by='schedule.schedule_id',
                         back_populates='subj')


class teachers(Base):
    __tablename__ = 'teachers'
    teachers_id = Column(Integer, primary_key=True)
    name = Column(String)
    home_address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    sched  = relationship("schedule", order_by='schedule.schedule_id',
                         back_populates='teach')

class students(Base):
    __tablename__ = 'students'
    students_id = Column(Integer, primary_key=True)
    name = Column(String)
    home_address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    sched  = relationship("schedule", order_by='schedule.schedule_id',
                         back_populates='stud')


class schedule(Base):
    __tablename__ = 'schedule'
    schedule_id = Column(Integer, primary_key=True)
    subjects_id = Column(Integer, ForeignKey('subjects.subjects_id'))
    teachers_id = Column(Integer, ForeignKey('teachers.teachers_id'))
    students_id = Column(Integer, ForeignKey('students.students_id'))
    week_day = Column(String)
    subj  = relationship("subjects", back_populates="sched")
    teach = relationship("teachers", back_populates="sched")
    stud  = relationship("students", back_populates="sched")
        
                         

class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def insert_data(table_name, values):
        if  table_name  == 'subjects':
            session.add(subjects(subjects_id=values[0], name=values[1]))
            session.commit()
            
        elif table_name == 'teachers':
            session.add(teachers(teachers_id=values[0], name=values[1],
                                 home_address=values[2], phone_number=values[3],
                                 email=values[4]))
            session.commit()
            
        elif table_name == 'students':
            session.add(students(students_id=values[0], name=values[1],
                                 home_address=values[2], phone_number=values[3],
                                 email=values[4]))
            session.commit()
            
        elif table_name == 'schedule':
            session.add(schedule(schedule_id=values[0], subjects_id=values[1],
                                 teachers_id=values[2], students_id=values[3],
                                 week_day=values[4]))
            session.commit()


    @staticmethod
    def delete_data(table_name, del_id):
        if  table_name  == 'subjects':
            session.query(subjects).filter_by(subjects_id=del_id).delete()
            session.commit()

        elif table_name == 'teachers':
            session.query(teachers).filter_by(teachers_id=del_id).delete()
            session.commit()

        elif table_name == 'students':
            session.query(students).filter_by(students_id=del_id).delete()
            session.commit()
            
        elif table_name == 'schedule':
            session.query(schedule).filter_by(schedule_id=del_id).delete()
            session.commit()

    @staticmethod
    def update_data(table_name, values):
        if  table_name  == 'subjects':
            session.query(subjects).filter_by(subjects_id=values[0]).update({subjects.name: values[1]})
            session.commit()

        elif table_name == 'teachers':
            session.query(teachers).filter_by(teachers_id=values[0]).update({teachers.name: values[1],
                                                                             teachers.home_address: values[2],
                                                                             teachers.phone_number: values[3],
                                                                             teachers.email: values[4]})
           
            session.commit()

        elif table_name == 'students':
            session.query(students).filter_by(students_id=values[0]).update({students.name: values[1],
                                                                             students.home_address: values[2],
                                                                             students.phone_number: values[3],
                                                                             students.email: values[4]})
            session.commit()
            
        elif table_name == 'schedule':
            session.query(schedule).filter_by(schedule_id=values[0]).update({schedule.week_day: values[1]})
            session.commit()
