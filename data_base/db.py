from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base.models import Base, User, Goal


class DBHelper:

    def __init__(self):
        self.engine = create_engine("mysql://root:pass@localhost/dbfile")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def user_regist(self, user_id):
        self.session.rollback()
        is_regist = self.session.query(User).filter_by(id=user_id).first()
        return is_regist

    def add_user(self, user_id, username, first_name, age, city, description):
        self.session.add(
            User(id=user_id, username=username, first_name=first_name, age=age, city=city, description=description))
        self.session.commit()

    def add_goal(self, user_id, goal):
        user = self.session.query(User).filter_by(id=user_id).first()
        self.session.add(Goal(user_id=user.id, goal=goal))
        self.session.commit()
