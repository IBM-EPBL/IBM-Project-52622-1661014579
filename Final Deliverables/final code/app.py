from flask import Flask, request, render_template
import urlFeatures
import jsFeatures
import domainFeatures
import pickle
from features import FeatureExtraction
import numpy as np

app = Flask(__name__, static_url_path="/static")
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "" #hidden because of security reasons
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST" and "url" in request.form:
        url = request.form.get("url")
        features = []
        features.extend(urlFeatures.fetchURLFeatures(url))
        features.extend(jsFeatures.fetchJSFeatures(url))
        features.extend(domainFeatures.fetchDomainFeatures(url))
        features = np.array(features)
        features = features.reshape(1, -1)
        loaded_model = pickle.load(open("XGBoostClassifier.pkl", "rb"))
        result = loaded_model.predict(features)
        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,13)
        print(x)
        t=[obj.getFeaturesList()]
        print("t")
        print(t)
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": [['f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']], "values": t}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/149au568-d842-2745-9dbe-60431g7h0918/predictions?version=2022-11-11', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})

        if result[0] == -1:
            msg = "FAILED"
        else:
            msg = "SUCCESS"

        return render_template('index.html', msg=msg)

    else:
        return render_template("index.html", msg="")


if __name__ == '__main__':
    app.run(debug=False)