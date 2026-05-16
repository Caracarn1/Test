from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>My Webpage</title></head>
    <body style="text-align:center; font-family:Arial;">
        <h1>Hello from Render!</h1>
        <p>My Python webpage is working.</p>
        <img src="https://photojournal.jpl.nasa.gov/jpeg/PIA18033.jpg"
             alt="Earth from NASA"
             style="width:80%; max-width:800px; margin-top:20px;">
        <p><small>Image credit: NASA/JPL</small></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
