from flask import Flask, request
from user import user
from business import business

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET', 'PUT'])
def login():
    if request.method == 'POST' or request.method == 'GET':
        args = [key for key in request.form.keys()]
        print(args)
        access_token = request.args.get('t')
        u = user('')
        print(u.get_birthdays())
    elif request.method == 'PUT':
        args = [key for key in request.form.keys()]
        print(args)
    return ""

if __name__ == '__main__':
    # business_db = business('root', 'sugiff16', '127.0.0.1', 3300, 'business')
    # TEST
    # business_id = business_db.create_business('business_test', 'business_test123')
    # products = business_db.create_product('product_test', 4.99, 'a', business_id)
    # print(products)
    # END TEST
    # business_db.close()
    app.run()