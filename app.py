from MVT import create_app

app = create_app()

if __name__ == "__main__":
    app.db.create_all()
    app.run(debug=True)
