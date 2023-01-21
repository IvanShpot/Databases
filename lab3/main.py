from orm import Base, engine
from controller import Controller
from sqlalchemy import MetaData


metadata = MetaData()
Base.metadata.create_all(engine)
Controller.menu()
