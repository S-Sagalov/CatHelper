from sqlalchemy import Column, Text, Integer, ForeignKey

from app.core.db import AbstractMoneyAndDate


class Donation(AbstractMoneyAndDate):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
