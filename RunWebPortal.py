from app import app

# Do not set debug=True when webportal is live or you could be exposing yourself to the horrors of the internet!


def go():
    app.run(debug=False)
