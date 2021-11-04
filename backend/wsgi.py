from app import app, db

if __name__ == '__main__':
    if not db.engine.dialect.has_table(db.engine.connect(), "signs"):
        db.create_all()
    app.run(debug=False)
