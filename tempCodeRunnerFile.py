









# Create Database in Main method

if __name__ == "main":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
