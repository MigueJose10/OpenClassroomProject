import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, roc_auc_score, precision_score, roc_curve, recall_score, classification_report
from sklearn.metrics import make_scorer
from sklearn.impute import SimpleImputer
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
data_stat =pd.read_csv('data_dashboard.csv', index_col='SK_ID_CURR')
data_stat_imp = imputer.fit(data_stat)
@app.route('/predict/<int:client_id>')
def predict(client_id):
    x =data.loc[client_id].values.reshape(1, -1)
    pred = model.predict(x)[0]
    proba_pay = model.predict_proba(x)[0][0]*100
    proba_pay = f'{proba_pay:.4}'
    print(proba_pay)

    return render_template('dashboard.html', client_id=client_id, pred=pred, proba_pay=proba_pay )



if __name__ == "__main__":
    app.run(debug=True)
