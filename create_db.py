from flask import Flask
from models import log, db, Tarifs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        artist1 = Tarifs(name='Казах', teacher="Жарылкаганов Нурмухаммед", description="Самый обычный тариф, к концу "
                                                                                       "курса станете стандартным "
                                                                                       "сигмой, как любой казах",
                         price=7000)
        artist2 = Tarifs(name='Патрик Бэтмэн', teacher="Байбаков Константин", description="Продвинутый курс, не факт, "
                                                                                          "что к концу станете "
                                                                                          "американцем и при этом еще "
                                                                                          "и психопатом, "
                                                                                          "но сигмой точно будете",
                         price=12000)
        artist3 = Tarifs(name='Томас Щебень', teacher="Походня Никита", description="Самый продвинутый курс, к концу "
                                                                                    "начнете нормально одеваться, "
                                                                                    "а может даже заговорите с "
                                                                                    "девочкой!", price=20000)
        db.session.add_all([artist1, artist2, artist3])
        db.session.commit()

    print('Создана база данных users')