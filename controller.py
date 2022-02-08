from main import app

@app.route('/')
def index():
    return "Hooray"
@app.route('/fish/{id}')
def get_fish(id):
    print(id)
    return "my fish is gougerous"

@app.route("/fish")
def get_all_fishes():
    return "all fishes"

@app.route("/fish", methods = ["POST"])
def create_fish():
    print("fish created")
    return "fish created"