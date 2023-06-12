from flask import Flask, render_template, request, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# SQLAlchrmyの設定を記述する。composeファイルの環境変数で指定したとおり、データベース名や接続情報を指定する。
DB_USER = "docker"
DB_PASS = "docker"
DB_HOST = "db"
DB_NAME = "flask_app"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# DBのテーブルを定義する
class User(db.Model):
    # テーブル名を指定
    __tablename__ = 'Users'
    # 数値型のidカラム
    id = db.Column(db.Integer, primary_key=True)
    # 文字列型のnameカラム
    name = db.Column(db.String(128))


@app.route("/",methods=['GET'])
def index_get():
    return render_template('index.html')


# ユーザ一覧ページ
@app.route("/users",methods=['GET'])
def users_get():
    # ユーザオブジェクトを全て取得
    users = User.query.all()
    return render_template('users_get.html', users=users)


# ユーザー追加処理
@app.route("/users",methods=['POST'])
def users_post():
    # ブラウザから送信されたuser_nameをもとにオブジェクトを作成
    user = User(
        name=request.form["user_name"]
    )
    # オブジェクトをDBに追加
    db.session.add(user)
    # DBへの変更を保存
    db.session.commit()
    # ユーザー一覧ページへ移動（関数名users_getで指定する）
    return redirect(url_for('users_get'))


# ユーザー詳細ページ
@app.route("/users/<id>",methods=['GET'])
def users_id_get(id):
    # パスパラメータからidを取得し、idを指定してデータベースからユーザを取得する
    user = User.query.get(id)
    return render_template('users_id_get.html', user=user)

# ユーザー情報更新
@app.route("/users/<id>/edit",methods=['POST'])
def users_id_post_edit(id):
    # 指定されたIDのユーザオブジェクトを取得
    user = User.query.get(id)
    # ブラウザから送信されたuser_nameをもとにオブジェクトを修正
    user.name = request.form["user_name"]
    # 追加ではなく修正内容を適応
    db.session.merge(user)
    # DBへの変更の保存
    db.session.commit()
    return redirect(url_for('users_get'))

# ユーザー削除
@app.route("/users/<id>/delete",methods=['POST'])
def users_id_post_delete(id):
    # 指定されたIDのユーザオブジェクトを取得
    user = User.query.get(id)
    # オブジェクトを削除
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users_get'))

#いっしん
@app.route("/takeuchi", methods=['GET'])
def takeuchi_get():
    return render_template('5431.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)