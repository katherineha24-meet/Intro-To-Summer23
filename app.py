from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return '''
    <html>

        <h1>Welcome to the Photo Gallery!</h1>
        <p>this is a photo gallery containing three types of photos: food, pets, and outer space.</p>
        <a href = "/food1">go to the first food photo</a>
        <br>
        <a href = "/pet1">go to the first pet photo</a>
        <br>
        <a href = "/space1">go to the first space photo</a>


    </html>
    '''

@app.route("/food1")
def food1():
    return '''
    <html>

        <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Barbacoa_taco.jpg/1280px-Barbacoa_taco.jpg" width = "300px">
        <br>
        <a href = "/food2">Next food</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''

@app.route("/food2")
def food2():
    return '''
    <html>

        <img src = "https://fusedbyfionauyema.com/wp-content/uploads/2021/02/Fused-by-Fiona-Uyema-Sushi-Q-A-how-to-make-sushi-at-home.jpg" width = "300px">
        <br>
        <a href = "/food1">Previous food</a>
        <br>
        <a href = "/food3">Next food</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''

@app.route("/food3")
def food3():
    return '''
    <html>

        <img src = "https://www.telegraph.co.uk/content/dam/recipes/2021/02/19/chicken-burger_trans_NvBQzQNjv4BquzGXYkbn9MyIUBw1YyLhrijKpPnP_ePeEESwLXhh29g.png?imwidth=1280" width = "300px">
        <br>
        <a href = "/food2">Previous food</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''


@app.route("/pet1")
def pet1():
    return '''
    <html>

        <img src = "https://supremepetfoods.com/wp-content/uploads/2015/09/iStock-92365010-1200px.jpg.webp" width = "300px">
        <br>
        <a href = "/pet2">Next pet</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''

@app.route("/pet2")
def pet2():
    return '''
    <html>

        <img src = "https://cdn.theatlantic.com/thumbor/OgQgHFiqAd92pArI1zjmcUHjoSc=/144x0:2411x1700/1200x900/media/img/mt/2017/06/shutterstock_319985324/original.jpg" width = "300px">
        <br>
        <a href = "/pet1">Previous pet</a>
        <br>
        <a href = "/pet3">Next pet</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''

@app.route("/pet3")
def pet3():
    return '''
    <html>

        <img src = "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg" width = "300px">
        <br>
        <a href = "/pet2">Previous pet</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''


@app.route("/space1")
def space1():
    return '''
    <html>

        <img src = "https://c.files.bbci.co.uk/16BB/production/_110891850_pia23645_index.jpg" width = "300px">
        <br>
        <a href = "/space2">Next space</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''

@app.route("/space2")
def space2():
    return '''
    <html>

        <img src = "https://media.istockphoto.com/id/1035676256/photo/background-of-galaxy-and-stars.jpg?s=612x612&w=0&k=20&c=dh7eWJ6ovqnQZ9QwQQlq2wxqmAR7mgRlQTgaIylgBwc=" width = "300px">
        <br>
        <a href = "/space1">Previous space</a>
        <br>
        <a href = "/space3">Next space</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''

@app.route("/space3")
def space3():
    return '''
    <html>

        <img src = "https://i.natgeofe.com/k/1ef0d42f-adf7-49e7-a2de-7d381fd18f95/moon-landing-textimage_square.png" width = "300px">
        <br>
        <a href = "/space2">Previous space</a>
        <br>
        <a href = "/home">Back to home</a>

    </html>'''


if __name__ == '__main__':
    app.run(debug=True)