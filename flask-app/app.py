import os
from flask import Flask
app = Flask(__name__)

# can I build a map of configurations where the one layer has the capability of overriding the previous one?
# defaults <- file contents <- environments variables and/or cmd parameters

# default value
lines = "no contents"

# updates with a config file
with open('contents.txt') as f:
    lines = f.readlines()

# overrided with an env variable or command line parameter
contents = os.environ.get('CONTENTS', '\n'.join(lines))

@app.route('/')
def hello_geek():
    return contents


if __name__ == "__main__":
    app.run(debug=True)