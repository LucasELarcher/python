from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .operacoes import Operacao

__all__ = ["db", "Operacao"]
