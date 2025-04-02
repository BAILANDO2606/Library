from flask import Flask, render_template, jsonify
import json

app = Flask(__name__, static_folder='my_flask_project/static')

books = {
    1: "Мій власний текст книги 'Війна і мир'...",
    2: "Оновлений текст для 'Теорія всього'...",
    3: "Текст для 'Відьмак. Останнє бажання'...",
    4: "Власний текст для 'До останнього подиху'...",
    5: "Ще один власний текст для 'Мистецтво війни'..."
}


with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)


@app.route('/get_book/<int:book_id>')
def get_book(book_id):
    book_text = books.get(book_id, "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.") 
    return jsonify({"text": book_text})

@app.route("/book1")  # Додаємо маршрут для book1.html
def book1():
    return render_template("book1.html")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/catalog')
def catalog():
    return "<h1>Catalog Page</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"

@app.route('/faq')
def faq():
    return "<h1>FAQ Page</h1>"

@app.route('/blog')
def blog():
    return "<h1>Blog Page</h1>"

@app.route('/events')
def events():
    return "<h1>Events Page</h1>"

@app.route('/testimonials')
def testimonials():
    return "<h1>Testimonials Page</h1>"

@app.route('/careers')
def careers():
    return "<h1>Careers Page</h1>"

@app.route('/partners')
def partners():
    return "<h1>Partners Page</h1>"

@app.route('/search')
def search():
    return "<h1>Search Results Page</h1>"

@app.route('/category/<category>')
def category(category):
    return f"<h1>Category: {category.capitalize()}</h1>"

@app.route('/privacy_policy')
def privacy_policy():
    return "<h1>Privacy Policy Page</h1>"

@app.route('/terms_of_service')
def terms_of_service():
    return "<h1>Terms of Service Page</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5015)