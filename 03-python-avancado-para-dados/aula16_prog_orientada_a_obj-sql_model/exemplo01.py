from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# Conectar ao SQLite em memória
engine = create_engine("sqlite:///meubanco.db", echo=True)

# dialetos
# engine = create_engine(
#     "postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase"
# )

print("Conexão com SQLite estabelecida.")

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(Integer)


# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)
