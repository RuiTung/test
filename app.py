import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mysqldb import MySQL
from wtforms import Form, TextAreaField, validators
from functools import wraps
from datetime import datetime

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'us-cdbr-east-02.cleardb.com'
app.config['MYSQL_USER'] = 'b30f91d5550828'
app.config['MYSQL_PASSWORD'] = '2a11f5c2'
app.config['MYSQL_DB'] = 'heroku_4188fbcf1472bbd'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'super secret key'

# init MYSQL
mysql = MySQL(app)

# home page
@app.route('/')
def home():
    return render_template('home.html')


# view tweets
@app.route('/tweets')
def tweets():
    # creat cursor
    cur = mysql.connection.cursor()

    # get tweets
    result = cur.execute("SELECT * FROM tweets")

    tweets = cur.fetchall()

    if result > 0:
        return render_template('tweets.html', tweets = tweets)
    else:
        msg = "No tweets found"
        return render_template('tweets.html', msg = msg)
    #close connection
    cur.close()

# view comments of a tweet
@app.route('/comments/<string:id>/')
def comments(id):
    # creat cursor
    cur = mysql.connection.cursor()
    
    # get comments
    result = cur.execute("SELECT * FROM comments WHERE tweetsID = %s", [id])

    comments = cur.fetchall()

    if result > 0:
        return render_template('comments.html', comments = comments)
    else:
        msg = "No comments found"
        return render_template('comments.html', msg = msg)

    #close connection
    cur.close()


# tweet form class
class TweetForm(Form):
    content = TextAreaField('Content', [validators.Length(min = 10)])

# add tweet
@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    form = TweetForm(request.form)
    if request.method == 'POST' and form.validate():
        content = form.content.data
    
        # create cursor
        cur = mysql.connection.cursor()

        # execute
        cur.execute("INSERT INTO tweets(content, create_date) VALUES(%s, %s)", (content, datetime.now()))

        # commit to db
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('Tweet Created', 'success')

        return redirect(url_for('tweets'))
    return render_template('add_tweet.html', form = form)

# comment form class
class CommentForm(Form):
    comment = TextAreaField('Comment', [validators.Length(min = 10)])

# add comment to a tweet
@app.route('/add_comment/<string:id>', methods=['GET', 'POST'])
def add_comment(id):
    form = CommentForm(request.form)
    if request.method == 'POST' and form.validate():
        comment = form.comment.data
    
        # create cursor
        cur = mysql.connection.cursor()

        # execute
        cur.execute("INSERT INTO comments(tweetsID, content, create_date) VALUES(%s, %s, %s)", ([id], comment, datetime.now()))

        # commit to db
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('Comment Created', 'success')

        return redirect(url_for('comments', id = id))
    return render_template('add_comment.html', form = form)


if __name__=='__main__':
    app.run(debug=True)