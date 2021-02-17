import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, roc_auc_score, precision_score, roc_curve, recall_score, classification_report
from sklearn.metrics import make_scorer
import json
import pandas as pd

def cost(truth, preds):
    precision = precision_score(truth, preds)
    recall = recall_score(truth, preds)
    # square beta
    beta2 = 2.5**2
    f_mesure = ((1+beta2)*precision*recall)/(beta2*(precision+recall))
    return f_mesure

custom_scorer = make_scorer(cost, greater_is_better=False)

app = Flask(
    __name__,
    static_url_path='/static', static_folder='static',
    template_folder='templates')

model = pickle.load(open('model_lr.sav', 'rb'))
data = pd.read_csv('data_model_red.csv', index_col='index')
data_stat = pd.read_csv('data_dashboard.csv', index_col='SK_ID_CURR')
counts_read = pd.read_csv('installements.csv', index_col='index')


with open('result.json') as json_file:
    result = json.load(json_file)



@app.route('/predict/<int:client_id>')
def predict(client_id):
    x =data.loc[client_id].values.reshape(1, -1)
    pred = model.predict(x)[0]
    proba_pay = model.predict_proba(x)[0][0]*100
    proba_pay = f'{proba_pay:.4}'
    curr_client_count = counts_read.loc[client_id][0]

    print(proba_pay)
    #print(result)
    print(curr_client_count)

    return render_template(
        'dashboard.html', client_id=client_id, pred=pred, proba_pay=proba_pay,
        result=json.dumps(result), curr_client_count=curr_client_count)


@app.route('/')
def hello():
    return 'Scoring Model Home'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
