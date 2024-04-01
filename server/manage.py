from flask.cli import FlaskGroup
from api import create_app, db
from api.models import *

application = create_app()
cli = FlaskGroup(application)


@cli.command("init_db")
def init_db():
    """初始化数据库"""
    # db.drop_all()
    db.create_all()
    print("数据库初始化成功")


if __name__ == "__main__":
    cli()
