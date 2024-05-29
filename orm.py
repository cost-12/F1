from sqlalchemy import create_engine, Column, String, Float 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

class Car(Base):
    __tablename__ = "car"
    Equipe = Column(String, primary_key=True) 
    Chassi = Column(Float, nullable=False)
    Aerodinamica = Column(Float, nullable=False)
    Motor = Column(Float, nullable=False)
    Durabilidade = Column(Float, nullable=False)

Base.metadata.create_all(engine)

def adiciona_car(Equipe, Chassi, Aerodinamica, Motor, Durabilidade):
    Session = sessionmaker(bind=engine)
    session = Session()
    car = Car(Equipe=Equipe, Chassi=Chassi, Aerodinamica=Aerodinamica, Motor=Motor, Durabilidade=Durabilidade)
    session.add(car)
    session.commit()
    session.close()

#adiciona_car("AndrettiCadillac", 4.1, 5.2, 9.8, 7.5)
#adiciona_car("Bugatti F1 Team", 8.1, 8.2, 9.8, 9.5)

def atualiza_car(Equipe=None, Chassi=None, Aerodinamica=None, Motor=None, Durabilidade=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    car = session.query(Car).filter_by(Equipe=Equipe).first()
    if car:
        car.Chassi = Chassi
        car.Aerodinamica = Aerodinamica
        car.Motor = Motor
        car.Durabilidade = Durabilidade
        session.commit()
        session.close()

def deletar_car(Equipe):
    Session = sessionmaker(bind=engine)
    session = Session()
    car = session.query(Car).filter_by(Equipe=Equipe).first()
    if car:
        session.delete(car)
        session.commit()
        session.close()

deletar_car("Bugatti F1 Team")
