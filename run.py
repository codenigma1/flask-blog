# What is the difference between __init__.py and __main__.py?

# https://stackoverflow.com/questions/4042905/what-is-main-py

# https://stackoverflow.com/questions/448271/what-is-init-py-for


# https://stackoverflow.com/questions/31327762/what-is-the-difference-betweenin-py#:~:text=2%20Answers&text=__init__.py%20%2C%20among,allows%20you%20to%20execute%20packages.-init-py-and-ma

from flaskblog import app


if __name__ == '__main__':
    app.run(debug=True)