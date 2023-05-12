from config.TsrShopDetails_config import *


class TsrShopDetailsProject(Base):
    __tablename__ = "tsrshopdetails"
    Name = Column("name", String)
    Email = Column("email", String)
    City = Column("city", String)
    State = Column("state", String)
    Dealer = Column("dealer", String)
    Vehicle = Column("vehicle", String)
    Dealer_city = Column("dealer_city", String)
    Mobile_number = Column("mobile_number", Integer, primary_key=True)