from app import create_app

app = create_app()

@app.route("/")
def index():
    return "<p>Welcome to COMP90024</p>"

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT= 80
    DEBUG = True

    app.run(debug=DEBUG, host=HOST, port=PORT)