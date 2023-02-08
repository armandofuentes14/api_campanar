from django.http import HttpResponse
import sqlite3
from django.http import JsonResponse
import pickle
import pandas
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords


def index(request):
   return HttpResponse("""<h1>API datos campanar</h1>
                        <h2>Endpoints</h2>

                        <h3>/users</h3>
                        <p>0: id_user</p>
                        <p>1: name</p>
                        <p>2: surname</p>
                        <p>3: birthdate</p>
                        <p>4: email</p>
                        <p>5: codephone</p>
                        <p>6: phonenumber</p>
                        <p>7: password</p>
                        <p>8: image</p>
                        <p>9: role</p>

                        <h3>/news</h3>
                        <p>0: id_user</p>
                        <p>1: title</p>
                        <p>2: body</p>
                        <p>3: image</p>
                                
                        <h3>/requests</h3>
                        <p>0: id_user</p>
                        <p>1: cathegory</p>
                        <p>2: title</p>
                        <p>3: body</p>
                        <p>4: image</p>
                        <p>5: address</p>

                        <h3>/activities</h3>
                        <p>0: title</p>
                        <p>1: body</p>
                        <p>2: image</p>
                        <p>3: adress</p>
                        <p>4: date</p>
                        <p>5: id_user</p>

                        <h3>/predict</h3> 

                        <h3>/sentiment</h3>                       
                        """)

def get_users(request):
    connection = sqlite3.connect('datos.db')
    cursor = connection.cursor()
    select_users = """SELECT * 
                    FROM usuarios"""
    result = cursor.execute(select_users).fetchall()
    connection.close()
    return JsonResponse(result,safe=False)

# 2.Ruta para obtener todos las noticias
def get_news(request):
    connection = sqlite3.connect('datos.db')
    cursor = connection.cursor()
    select_news = """SELECT * 
                    FROM noticias"""
    result = cursor.execute(select_news).fetchall()
    connection.close()
    return JsonResponse(result,safe=False)

# 3.Ruta para obtener todos las peticiones
def get_requests(request):
    connection = sqlite3.connect('datos.db')
    cursor = connection.cursor()
    select_peticiones = """SELECT * 
                    FROM peticiones"""
    result = cursor.execute(select_peticiones).fetchall()
    connection.close()
    return JsonResponse(result,safe=False)

# 4.Ruta para obtener todos las actividades
def get_activities(request):
    connection = sqlite3.connect('datos.db')
    cursor = connection.cursor()
    select_actividades = """SELECT * 
                    FROM actividades"""
    result = cursor.execute(select_actividades).fetchall()
    connection.close()
    return JsonResponse(result,safe=False)

# 5. Ruta para predecir categorias de noticias
def get_prediction(request):
    #Load test DF
    test_df = 'La Universidad Popular contará'
    # Download stopwords
    nltk.download('stopwords')
    # Get the Spanish stopwords
    stopwords_list = stopwords.words('spanish')
    # Preprocess the text data using a CountVectorizer 
    vectorizer = pickle.load(open("vectorizer_theme_news_v1.1.pkl", 'rb'))
    #Load model
    model = pickle.load(open('model_theme_news_v1.1.pkl','rb'))
    #Predict
    new_text = [test_df]
    new_text = vectorizer.transform(new_text)
    prediction = model.predict(new_text)
    return JsonResponse(list(prediction),safe=False)

# 6. Ruta para hacer sentiment analysis de las requests
def get_sentiment(request):
    test_df = 'Muy descontentod con la falta de interes'
    vectorizer = pickle.load(open("sentiment_vectorizer.pkl", 'rb'))
    model = pickle.load(open('sentiment_model.pkl','rb'))
    new_text = [test_df]
    new_text = vectorizer.transform(new_text)
    prediction = model.predict(new_text)
    result = 'Positivo' if prediction == 1 else 'Negativo'
    return JsonResponse(list(result),safe=False)
