from flask import Flask, request, render_template_string

app = Flask(__name__)

users = {}

html_form='''
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login Form</h2>
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit" name="action" value="Login">Login</button>
        <button type="submit" name="action" value="Signup">Signup</button>
    </form>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(html_form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    action = request.form['action']

    if action == "Signup":
        if username in users:
            return f"<h3 style='color:red;'>Username '{username}' already exists. Try logging in.</h3>"
        users[username] = password
        return f"<h3>Signup successful for user: {username}</h3>"

    elif action == "Login":
        if username not in users:
            return f"<h3 style='color:red;'>Username '{username}' not found. Please sign up first.</h3>"
        if users[username] != password:
            return f"<h3 style='color:red;'>Incorrect password for user: {username}</h3>"
        return f"<h3>Welcome back, {username}!</h3>"

    else:
        return "<h3>Unknown action.</h3>"

print(users)

if __name__ == '__main__':
    app.run(debug=True)