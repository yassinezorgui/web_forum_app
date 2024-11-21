from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Classes

class user:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def subscribe(self):
        pass

    def connect(self):
        pass

    def post(self, thread, post):
        thread.add(post)

    def reply(self, thread, post):
        thread.add(post)


class mod(user):
    def __init__(self, username, password, email, privilege=True):
        super().__init__(username, password, email)
        self.privilege = privilege

    def modify(self, thread, post):
        for p in thread.posts:
            if p == post:
                pass

    def delete(self, thread, post):
        thread.posts = [p for p in thread.posts if p != post]


class thread:
    def __init__(self, title, creation_date):
        self.title = title
        self.creation_date = creation_date
        self.posts = []

    def add(self, post):
        self.posts.append(post)

    def __str__(self):
        return f"Thread: {self.title}, Created on: {self.creation_date}, Posts: {[str(p) for p in self.posts]}"


class post:
    def __init__(self, caption, author, publication_date):
        self.caption = caption
        self.author = author
        self.publication_date = publication_date

    def __str__(self):
        return f"Post by {self.author} on {self.publication_date}: {self.caption}"


class file_post(post):
    def __init__(self, caption, author, publication_date, attached_file, file_type):
        super().__init__(caption, author, publication_date)
        self.attached_file = attached_file
        self.file_type = file_type

    def __str__(self):
        return f"{super().__str__()}, Attached file: {self.attached_file} ({self.file_type})"


class file:
    def __init__(self, name, size, file_type):
        self.name = name
        self.size = size
        self.file_type = file_type

    def delete(self):
        pass

    def __str__(self):
        return f"File: {self.name}, Size: {self.size}, Type: {self.file_type}"


class image(file):
    def __init__(self, name, size, resolution):
        super().__init__(name, size, "image")
        self.resolution = resolution

    def adjust(self):
        pass

    def __str__(self):
        return f"{super().__str__()}, Resolution: {self.resolution}"

class GIF(image):
    def __init__(self, name, size, resolution, duration):
        super().__init__(name, size, resolution)
        self.duration = duration  

    def __str__(self):
        return f"{super().__str__()} (Type: GIF), Duration: {self.duration}s"


class JPG(image):
    def __init__(self, name, size, resolution, compression_rate):
        super().__init__(name, size, resolution)
        self.compression_rate = compression_rate  

    def __str__(self):
        return f"{super().__str__()} (Type: JPG), Compression Rate: {self.compression_rate}%"
    
    # Simulated database
users = {
    "user1": {"username": "Yassine", "role": "user"},
    "mod1": {"username": "Hatem", "role": "moderator"}
}
threads = []

# Routes
@app.route('/')
def home():
    return render_template("index.html", threads=threads)

@app.route('/thread/<int:thread_id>')
def view_thread(thread_id):
    thread = threads[thread_id]
    return render_template("thread.html", thread=thread, thread_id=thread_id)

@app.route('/post', methods=['POST'])
def post():
    thread_id = int(request.form['thread_id'])
    author = request.form['author']
    content = request.form['content']
    new_post = {"author": author, "content": content}
    threads[thread_id]["posts"].append(new_post)
    return redirect(url_for('view_thread', thread_id=thread_id))

@app.route('/moderate', methods=['POST'])
def moderate():
    thread_id = int(request.form['thread_id'])
    post_id = int(request.form['post_id'])
    action = request.form['action']
    if action == "delete":
        del threads[thread_id]["posts"][post_id]
    return redirect(url_for('view_thread', thread_id=thread_id))

if __name__ == '__main__':
    # Sample thread for testing
    threads.append({"title": "Recettes de Gâteaux", "posts": []})
    app.run(debug=True)

