from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html')

"""
@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'method is POST'
    else:
        return 'method is GET'

#examples to put variables string in URL
@app.route('/profile/<username>')
def profile(username):
    return '<h2> Name Is {} </h2>'.format(username)
#examples to put variables int (have to mention variable type) in URL
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h3> Post number is {} </h3>'.format(post_id)
"""

if __name__ == '__main__':
    app.run(debug=True)
