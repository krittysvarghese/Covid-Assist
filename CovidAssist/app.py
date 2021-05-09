
from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = 'powerful key'
string=''
@app.route('/')
def index():
    url="https://www.mohfw.gov.in/"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    div = soup.find("span", {"class": "coviddata"})
    val=div.text
    div1 = soup.find_all(class_ = "mob-hide")
    x=0
    for i in div1:
        x=x+1
        if(x==2):
            active=i.text
        elif(x==4):
            dis=i.text
        elif(x==6):
            death=i.text
    active, sep, tail = active.partition('\xa0')
    dis, sep, tail = dis.partition('\xa0')
    death, sep, tail = death.partition('\xa0')    
    return render_template("index.html",val=val,active=active,dis=dis,death=death)

@app.route('/plasma/',methods=['GET', 'POST'])
def plasma():
    return render_template("plasma.html")

@app.route('/state/',methods=['GET', 'POST'])
def state():
    
    return render_template("state.html")


@app.route('/oxygen/',methods=['GET', 'POST'])
def oxygen():
    if request.method == "POST":
        state = request.form.get("inputState")
        dist = request.form.get("inputDistrict") 
        state=str(state)
        url1= "https://dir.indiamart.com/search.mp?ss=portable+oxygen+cylinders+refil "+dist
        url2= "https://dir.indiamart.com/search.mp?ss=oxygen+concentrator "+dist
        url3 ="https://www.google.com/search?q=oxygen+bed+availability+near+"+dist
        return render_template("oxygen.html",url1=url1,url2=url2,url3=url3)

@app.route('/doc/',methods=['GET', 'POST'])
def doc():
    return render_template("doc.html")

@app.route('/food/',methods=['GET', 'POST'])
def food():
    return render_template("food.html")

@app.route('/hospitals/',methods=['GET', 'POST'])
def hospitals():
    return render_template("hospitals.html")

@app.route('/news/',methods=['GET', 'POST'])
def news():
    return render_template("news.html")

@app.route('/containment_zone/',methods=['GET', 'POST'])
def containmengt_zone():
    return render_template("containment_zone.html")

@app.route('/state2/',methods=['GET', 'POST'])
def state2():
    return render_template("state2.html")

@app.route('/icu/',methods=['GET', 'POST'])
def icu():
    if request.method == "POST":
        state = request.form.get("inputState")
        dist = request.form.get("inputDistrict") 
        state=str(state)
        url1= "https://twitter.com/search?q=verified%20icu%20"+state+"&src=typed_query&f=live"
        url2= "https://www.google.com/search?q=icu+near+"+dist
        url3 ="https://twitter.com/search?q=verified%20hospital%20bed%20"+state+"&src=typed_query&f=live"
        url4 ="https://www.google.com/search?q=hospital+bed+near+"+dist
        url5 ="https://twitter.com/search?q=verified%20home%20icu%20"+state+"&src=typed_query&f=live"
        url6 ="https://www.google.com/search?q=home+icu+near+"+dist
        url7 ="https://twitter.com/search?q=verified%20ventilator%20"+state+"%20&src=typed_query&f=live"
        url8 ="https://www.google.com/search?q=ventilator+near+"+dist
        return render_template("icu.html",url1=url1,url2=url2,url3=url3,url4=url4,url5=url5,url6=url6, url7=url7,url8=url8)

@app.route('/chelpline/',methods=['GET', 'POST'])
def chelpline():
    return render_template("covid_helpline.html")

@app.route('/helpline/',methods=['GET', 'POST'])
def helpline():
    return render_template("helpline.html")

@app.route('/medicine/',methods=['GET', 'POST'])
def medicine():
    return render_template("medicine.html")

@app.route('/state_sites/',methods=['GET', 'POST'])
def state_sites():
    return render_template("state_websites.html")

@app.route('/stat/',methods=['GET', 'POST'])
def stat():
    if request.method == "POST":
        global string
        state = request.form.get("inputState")
        string=str(state)
        url1="https://coronaclusters.in/"+string
        html_content = requests.get(url1).text
        soup2 = BeautifulSoup(html_content, "lxml")

        data2= soup2.find_all(class_ = "card-title text-md text-md-lg")

        y=0
        for i in data2:
            y=y+1
            if(y==1):
                confirmed2=i.text
            if(y==2):
                act2 = i.text
            if(y==3):
                recovered2 = i.text

        return render_template("stat.html",confirmed2=confirmed2,act2=act2,recovered2=recovered2,state=state)

@app.route('/stat2/',methods=['GET', 'POST'])
def stat2():
    if request.method == "POST":
        district = request.form.get("dist")
        district=str(district)
        string1=district
        string2=string
        url="https://coronaclusters.in/"+string2+'/'+string1
        html_content2 = requests.get(url).text
        soup = BeautifulSoup(html_content2, "lxml")
        confirmed=''
        act=''
        recovered=''
        data= soup.find_all(class_ = "card-title text-md text-md-lg")
        y=0
        for i in data:
            y=y+1
            if(y==1):
                confirmed=i.text
            if(y==2):
                act = i.text
            if(y==3):
                recovered = i.text
        return render_template("stat2.html",confirmed=confirmed,act=act,recovered=recovered,district=district,string2=string2)
   

if __name__ == '__main__':
    app.run(debug=True)