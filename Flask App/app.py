from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        if request.form == 'POST' or 'GET':
            a = request.form['customer_id']
            b = request.form['customer_age']
            c = request.form['customer_income']
            d = request.form['home_ownership']
            e = request.form['employment_duration']
            f = request.form['loan_intent']
            h = request.form['loan_grade']
            i = request.form['loan_amnt']
            j = request.form['loan_int_rate']
            l = request.form['term_years']
            m = request.form['historical_default']
            n = request.form['cred_hist_length']
            inp = [float(a),float(b),float(c),float(d),float(e),float(f),float(h),float(i),float(j),float(l),float(m),float(n)]
        
            print(inp)
            with open('model/loan_svc.pkl', 'rb') as f:
                model = pickle.load(f)
            res = model.predict([inp])
            print(res)
            if res == 0:
                msg = 'DEFAULT'
            else:
                msg = 'NO DEFAULT'
            return render_template('pred.html', msg1=msg)
        return render_template('pred.html')
    except:
        return render_template('pred.html')

if __name__ == '__main__':
    app.run(debug=True)