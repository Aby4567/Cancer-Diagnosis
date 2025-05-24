from flask import Flask, render_template, flash, request, session, send_file
import pickle
import numpy as np
import mysql.connector
import sys
from keras.preprocessing import image

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AURemove")
def AURemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from regtb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('User  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/Blood")
def Blood():
    return render_template('Blood.html')


@app.route("/Lung")
def Lung():
    return render_template('LungCancer.html')


@app.route("/Skin")
def Skin():
    return render_template('Skin.html')


@app.route("/blood", methods=['GET', 'POST'])
def blood():
    if request.method == 'POST':
        import tensorflow as tf
        import cv2

        file = request.files['file']
        file.save('static/upload/Test.png')
        fname = 'static/upload/Test.png'
        img1 = cv2.imread('static/upload/Test.png')
        dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
        noi = 'static/upload/noi.png'

        cv2.imwrite(noi, dst)

        import warnings
        warnings.filterwarnings('ignore')

        model = tf.keras.models.load_model('static/Model/bmodel.h5')
        test_image = image.load_img('static/upload/Test.png', target_size=(200, 200))
        img_array = image.img_to_array(test_image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize
        prediction = model.predict(img_array)
        ind = np.argmax(prediction)
        out = ''
        pre = ''

        if ind == 0:
            out = 'Acute lymphoblastic leukemia (ALL)'
            pre = "taking an anti-infective or anti-inflammatory medication"
        elif ind == 1:
            out = 'Acute myelogenous leukemia (AML)'
            pre = "Aloe Vera, Black cohosh,Chamomile"
        elif ind == 2:
            out = 'Chronic lymphocytic leukemia (CLL)'
            pre = "Limiting alcohol consumption Exercising regularly"
        elif ind == 3:
            out = 'Chronic myelogenous leukemia (CML)'
            pre = "Tyrosine kinase inhibitors (TKIs) like imatinib, dasatinib, nilotinib, bosutinib, and asciminib, which target the BCR-ABL1 protein. "
        elif ind == 4:
            out = 'Normal'
            pre = "Nil"

        return render_template('Answer.html', result=out, org=fname, noi=noi, pre=pre)


@app.route("/lungcancer", methods=['GET', 'POST'])
def lungcancer():
    if request.method == 'POST':
        import tensorflow as tf
        import cv2

        file = request.files['file']
        file.save('static/upload/Test.png')
        fname = 'static/upload/Test.png'
        img1 = cv2.imread('static/upload/Test.png')
        dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
        noi = 'static/upload/noi.png'

        cv2.imwrite(noi, dst)

        import warnings
        warnings.filterwarnings('ignore')

        model = tf.keras.models.load_model('static/Model/lmodel.h5')
        test_image = image.load_img('static/upload/Test.png', target_size=(224, 224))
        img_array = image.img_to_array(test_image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize
        prediction = model.predict(img_array)
        ind = np.argmax(prediction)
        out = ''
        pre = ''

        if ind == 0:
            out = 'adenocarcinoma'
            pre = "Treatment for lung adenocarcinoma, the most common type of lung cancer, depends on the stage and " \
                  "overall health, often involving surgery, chemotherapy, radiation therapy, targeted therapies, " \
                  "and immunotherapy, sometimes used in combination. "
        elif ind == 1:
            out = 'carcinoma'
            pre = "Immunotherapy: Uses drugs to boost the body's immune system to fight cancer, becoming increasingly " \
                  "important in NSCLC treatment. "
        elif ind == 2:
            out = 'normal'
            pre = "Nil"
        elif ind == 3:
            out = 'squamous'
            pre = "Early-stage SCC can often be treated with local treatments like surgery or cryosurgery. Advanced " \
                  "SCC may require more aggressive treatments, such as surgery, radiation therapy, chemotherapy, " \
                  "or immunotherapy. "

        return render_template('Answer.html', result=out, org=fname, noi=noi, pre=pre)


@app.route("/skin", methods=['GET', 'POST'])
def skin():
    if request.method == 'POST':
        import tensorflow as tf
        import cv2

        file = request.files['file']
        file.save('static/upload/Test.png')
        fname = 'static/upload/Test.png'
        img1 = cv2.imread('static/upload/Test.png')
        dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
        noi = 'static/upload/noi.png'

        cv2.imwrite(noi, dst)

        import warnings
        warnings.filterwarnings('ignore')

        model = tf.keras.models.load_model('static/Model/skinmodel.h5')
        test_image = image.load_img('static/upload/Test.png', target_size=(200, 200))
        img_array = image.img_to_array(test_image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize
        prediction = model.predict(img_array)
        print(prediction)
        #np.argmax(prediction)
        ind = np.argmax(prediction)
        out = ''
        pre = ''

        if ind == 0:

            out = "BasalCellCarcinoma"
            pre = "5-fluorouracil (5-FU)"
        elif ind == 1:

            out = "CutaneousT-celllymphoma"
            pre = "Bone marrow transplant"
        elif ind == 2:

            out = "DermatofibrosarcomaProtuberans"
            pre = "Radiation therapy"
        elif ind == 3:

            out = "KaposiSarcoma"
            pre = "Antiretroviral therapy for HIV also treats KS"

        elif ind == 4:

            out = "MerkelCellcarCinoma"
            pre = "Immunotherapy"
        elif ind == 5:

            out = "SebaceousGlandCarcinoma"
            pre = "dequate surgical excision"
        elif ind == 6:

            out = "SquamousCellCarcinoma"
            pre = "Photodynamic therapy"

        return render_template('Answer.html', result=out, org=fname, noi=noi, pre=pre)


@app.route("/ViewDoctor", methods=['GET', 'POST'])
def ViewDoctor():
    if request.method == 'POST':
        uname = session['uname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multitypecancerdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM regtb where username='" + uname + "' ")
        data = cur.fetchall()
        return render_template('UserHome.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
