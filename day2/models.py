from sqlalchemy import Column,Integer, String
from database import Base

#cretea database fir sqllite
class Books(Base):
#sqlclchemyspecifc thing tis, name the table
    __tablename__="books"
    id= Column(Integer, primary_key=True, index=True)
    title=Column(String)
    author=Column(String)
    desc=Column(String)
    rating=Column(Integer)

