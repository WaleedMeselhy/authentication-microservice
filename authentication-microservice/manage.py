import os
from flask_script import Manager

from app import blueprint
from app.main import create_app
from app.main.config import config_by_name
app = create_app(config_by_name[os.getenv('APP_SETTINGS')]
                 or config_by_name['dev'])

app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)


@manager.command
def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()
