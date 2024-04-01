from api import create_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request

# 创建 Flask 应用程序实例
app = create_app()


if __name__ == "__main__":
    # 在开发环境中运行 Flask 应用程序
    app.run(debug=True)
