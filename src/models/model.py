from sqlalchemy import Integer,String,BigInteger
from sqlalchemy.sql.schema import Column
from db.database import Base

# CREATING AN AADHAR RESIDENT ADDRESS INFORMATION

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer,primary_key=True)
    house = Column(String,nullable=False)
    street = Column(String,nullable=False)
    area = Column(String,nullable=False)
    landmark = Column(String,nullable=False)
    village = Column(String,nullable=False)
    pincode = Column(BigInteger,nullable=False)
    sub_district = Column(String,nullable=False)
    district = Column(String,nullable=False)
    state = Column(String,nullable=False)