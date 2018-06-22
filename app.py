from flask import Flask, request
app = Flask(__name__)
    class myClass():
        def __init__(self):
            self.HOST = "https://popsql.io/"
            self.DB = 'database'
            self.LOGIN = 'bootcamp'
            self.PASSWORD = 'bootcamp'

            self.empl_no = None
            self.birth_date = None
            self.first_name = None
            self.last_name = None
            self.gender = None
            self.hire_date = None

    def authenticate(self):
            p = {'jsonrpc': "2.0",
                 'method': "call",
                 'params': {
                     'db': self.DB,
                     'login': self.LOGIN,
                     'password': self.PASSWORD}
                 }

@app.route("/post", methods=['GET', 'POST'])
def post():

    sent_obj = myClass()

    sent_obj.empl_no = request.args.get('employee no')
    sent_obj.birth_date = request.args.get('birth date')
    sent_obj.first_name = request.args.get('first name')
    sent_obj.last_name = request.args.get('last name')
    sent_obj.gender = request.args.get('gender')
    sent_obj.hire_date = request.args.get('hire date')

if __name__ == "__main__":
    app.debug = True
    app.run()