# manage.py

from flask_script import Manager, Server

from application import create_app


manager = Manager(create_app())
manager.add_command("runserver", Server())

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run(
        # debug=True,
        # port=5555,
    )
