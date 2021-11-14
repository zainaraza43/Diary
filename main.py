'''
main.py
The driver code for the diary app
'''
from website import create_app

app = create_app() # Creates the app

if __name__ == '__main__':
    app.run(debug=True)

