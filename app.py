from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
 
app = Flask(__name__)


# PostgreSQL の接続設定（DockerのPostgreSQLコンテナと接続）
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@postgres_todo:5432/todo_db"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://user:password@localhost/todo_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# SQLAlchemy のインスタンスを作成
db = SQLAlchemy(app)

# DBの設定
#db.init_app(app)


# Todoリストのデータモデル
class Todo(db.Model):  #インスタンスのdbと、modelという
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    
with app.app_context():
    #from flask_app import models
    db.create_all()  # モデルに基づいてデータベーステーブルを作成

@app.route('/')
def home():
    return "Hello, ToDo App!"

#if __name__ == '__main__':
#   app.run(debug=True, host='0.0.0.0', port=5000)









