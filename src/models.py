from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session, relationship
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/truetrade', pool_size=10, max_overflow=20)

Base = declarative_base()

db_session = scoped_session(sessionmaker(bind=engine))


class Aluno(Base):
    __tablename__ = 'aluno'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    serie = Column(String(100), nullable=False)
    senha_hash = Column(String(255), nullable=False)
    telefone = Column(String(255), nullable=False)

    def set_senha_hash(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password_hash(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def serialize(self):
        dados = {
            'nome': self.nome,
            'serie': self.serie,
            'senha_hash': self.senha_hash,
            'telefone': self.telefone
        }
        return dados


class Professor(Base):
    __tablename__ = 'professor'
    id_professor = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    senha = Column(String(100), nullable=False)


class Objeto(Base):
    __tablename__ = 'objeto'
    id_objeto = Column(Integer, primary_key=True)
    nome_objeto = Column(String(100), nullable=False)
    descricao = Column(String(250), nullable=False)
    id = Column(Integer, ForeignKey('aluno.id'))


class Troca(Base):
    __tablename__ = 'troca'
    id_pedido = Column(Integer, primary_key=True)
    status_pedido = Column(String(20), nullable=False)
    data_pedido = Column(DateTime, nullable=False, server_default=func.now())
    id_aluno_interessado = Column(Integer, ForeignKey('aluno.id'))
    id_item_desejado = Column(Integer, ForeignKey('objeto.id_objeto'))
    id_item_oferecido = Column(Integer, ForeignKey('objeto.id_objeto'))

    # secondary='atividades_recursos' diz pro SQLAlchemy qual tabela ponte usar.
    recursos = relationship("Recurso", secondary="troca_recursos", back_populates="troca")
