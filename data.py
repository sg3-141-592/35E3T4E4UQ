from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///sites.db',
    connect_args={"check_same_thread": False}
)


Base = declarative_base()

class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    target = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def addSite(url, target):
    newEntry = Site(
        url=url,
        target=target
    )
    session.add(newEntry)
    session.commit()
    return True

def lookupSite(url):
    sites = session.query(Site.target).filter_by(url=url).first()
    if sites:
        return sites[0]
    else:
        return None