from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 123!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/something/<path:somepath>')
def show_path(somepath):
    return f'path : {somepath}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
    
if __name__ == '__main__':
    app.run(debug=True)