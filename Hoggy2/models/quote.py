from sqlalchemy import Column, Integer, String, Text
from random import randint
import Hoggy2.meta as meta

class Quote(meta.base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    body = Column(Text)

    @classmethod
    def get_quote(cls, id = None):
        if id is None:
            id = randint(1,meta.session.query(cls).count())
        return meta.session.query(cls).get(id)

    @classmethod
    def add_quote(cls, quote):
        new_quote = cls()
        new_quote.body = quote
        meta.session.add(new_quote)
        meta.session.commit()

        return new_quote.id

    def delete(self):
        meta.session.delete(self)
        meta.session.commit()
