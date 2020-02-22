from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api.v1.app import app
from models.base_model import Base

migrate = Migrate(app, Base)
manager = Manager(app)

manager.add_command('Base', MigrateCommand)


if __name__ == '__main__':
    manager.run()