from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+mysqldb://tEYfmUh6aFwMfdv.root:jju2ImUNodnpORbg@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test?ssl_mode=VERIFY_IDENTITY&ssl_ca=<CA_PATH>"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"ssl":{"ssl:True"}}
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

