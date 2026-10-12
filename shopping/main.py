from datetime import datetime

from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker

from database import Base, engine, User, Task

SessionLocal = sessionmaker(bind=engine)


def main():
    # dob = datetime.strptime('10.05.2000', '%d.%m.%Y').date()
    # user2 = User(username='user2', password='secret1234', email='user2@email.com', date_of_birth=dob)
    # with SessionLocal() as session:
    #     session.add(user2)
    #     print('Added' + user2.__repr__())
    #     session.commit()
    #     print('Commited' + user2.__repr__())
    #
    #
    # statement = (insert(User)
    #              .values(username='user3', password='secret1234', email='user3@email.com')
    #              .returning(User.user_id))
    # with SessionLocal() as session:
    #     result = session.execute(statement)
    #     inserted_id = result.scalar_one()
    #     session.commit()
    #     print(inserted_id)

    # user4 = User(username='user4', password='secret1234', email='user4@email.com')
    # user5 = User(username='user5', password='secret1234', email='user5@email.com')
    # with SessionLocal() as session:
    #     session.add_all([user4, user5])
    #     session.commit()

    task1 = Task(description='Description 1', priority=1, due_date='2025-11-10', assigned_user_id=1)
    task2 = Task(description='Description 2', priority=3, due_date='2026-05-05', assigned_user_id=7)
    task3 = Task(description='Description 3', priority=4, due_date='2026-10-10', assigned_user_id=8)
    task4 = Task(description='Description 4', priority=6, due_date='2026-12-03', assigned_user_id=7)
    task5 = Task(description='Description 5', priority=2, due_date='2026-10-10', assigned_user_id=1)

    with SessionLocal() as session:
        session.add_all([task1, task2, task3, task4, task5])
        session.commit()


def create_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":  # pragma: no cover
    create_db()
    main()
