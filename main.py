#to install the sqlite package enter the following command in terminal :sudo apt-get install -y libsqlite3-dev
from flask import Flask
from flask import request, url_for, redirect, session, render_template
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"


@app.route("/")
@app.route("/Configurations")
def accueil():
    from database import Config
    configs = Config.query.all()
    return render_template("accueil.html", configs=configs)


@app.route("/form_handler", methods=["POST"])
def form_handler():
    from database import Config
    config_text = request.form["name"]
    config_author = request.form["creator"]
    config_mutable = request.form["mutable"]
    config_date = request.form["date"]

    # Create a new config
    new_config = Config()
    new_config.name = config_text
    new_config.creator = config_author
    new_config.mutable = config_mutable
    new_config.date = config_date

    db.session.add(new_config)
    db.session.commit()

    return redirect(url_for("accueil"))


@app.route("/nouvelle_config")
def nouvelle_config():
    return render_template("nouvelle_config.html")


@app.route("/delete_config/<config_id>")
def delete_config(config_id):
    from database import Config
    to_delete = Config.query.filter_by(id=config_id).first()
    db.session.delete(to_delete)
    return redirect(url_for("accueil"))


@app.route("/export_config/<config_id>")
def export_config(config_id):
    from database import Config
    to_export = Config.query.filter_by(id=config_id).first()
    return render_template("export.html", config=to_export)


@app.route("/edit_config/<config_id>")
def edit_config(config_id):
    from database import Config
    to_edit = Config.query.filter_by(id=config_id).first()
    to_delete = Config.query.filter_by(id=config_id).first()
    db.session.delete(to_delete)
    return render_template("edit.html", config=to_edit)


if __name__ == "__main__":
    # Create the DB
    from database import db
    print("creating database")
    db.create_all()
    print("database created")
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)