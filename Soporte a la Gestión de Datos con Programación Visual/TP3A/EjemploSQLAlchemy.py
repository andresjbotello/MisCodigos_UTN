from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base() # Metadatos

class Persona(Base):
    __tablename__ = 'persona' # ----nombre de la tabla
    # Definimos las columnas de la tabla Persona
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)

# ---- datos sqlite en la carpeta actual
engine = create_engine('sqlite:///sqlalchemy_ejemplo0.db')
Base.metadata.bind = engine

#---- creamos una sesión para admin datos
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def creaTabla():
    # Crea todas las tablas definidas en los metadatos
    Base.metadata.create_all(engine)

def insertaReg():
    oper = Persona()
    oper.nombre = 'Juan Carlos'
    session.add(oper)
    oper = Persona()
    oper.nombre = 'Miguel'
    session.add(oper)
    session.commit() #---<<<<Graba

def insertaReg2():
    oper = Persona()
    oper.nombre = 'Pepito'
    session.add(oper)
    oper = Persona()
    oper.nombre = 'Chuck'
    session.add(oper)
    session.commit() #---<<<<Graba

def borrar_persona(id_persona):
    per=session.query(Persona).filter(Persona.id == id_persona).one() 
    if per is None:
        print("Persona no encontrada")
        return False
    else:
        session.delete(per) 
        session.commit()      
    
def consulta():
    lp = session.query(Persona).all() #--- lista
    print('Lista de personas:')
    for p in lp:
        print('Persona: ', p.id, p.nombre)

def borraTabla():
    Persona.__table__.drop(engine)
        
if __name__ == '__main__':
    creaTabla()
    insertaReg()
    insertaReg2()
    consulta()
    borrar_persona(4)
    consulta()
    borraTabla()
