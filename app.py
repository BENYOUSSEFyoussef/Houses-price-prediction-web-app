import flask
import pickle
import pandas as pd
import joblib


model_path = r'C:/Users/Minfo/Houses-price-prediction-web-app/preprocessing/linear_regression_model.pkl'
model = joblib.load(model_path)

app = flask.Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def main():
   if flask.request.method == 'POST':
        aai = flask.request.form['aai']
        aah = flask.request.form['aah']
        aan = flask.request.form['aan']
        aanb = flask.request.form['aanb']
        ap = flask.request.form['ap']
        
        input_data = pd.DataFrame([[aai, aah, aan, aanb, ap]],
                                  columns=['Avg. Area Income', 'Avg. Area House Age',
                                           'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
                                           'Area Population'])
        prediction = model.predict(input_data)[0]
        
        # Récupérer les nouvelles coordonnées du formulaire
        lat = float(flask.request.form.get('lat', 34.0522))  # Valeur par défaut
        lon = float(flask.request.form.get('lon', -118.2437))  # Valeur par défaut
        
        return flask.render_template('index.html',
                                    original_input={'Avg. Area Income': aai,
                                                    'Avg. Area House Age': aah,
                                                    'Avg. Area Number of Rooms': aan,
                                                    'Avg. Area Number of Bedrooms': aanb,
                                                    'Area Population': ap},
                                    result=prediction,
                                    lat=lat,
                                    lon=lon)
   return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()