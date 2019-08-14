from app import app

@app.route('/', methods=['GET'])
def index():
    return  '<br/>' * 5 + '<center><h1>It is place for html</h1></center>'
