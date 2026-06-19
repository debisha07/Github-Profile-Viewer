from flask import Flask , request , render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/main')
def validate_username() :
    username = request.args.get("username")
    if username == None or username.strip() == " ":
        return "Enter Valid Username"
    return load_profile(username)

def load_profile(username) :
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200  :
        return "Some Internal Error has occured"
    if response.status_code == 404 :
        return "User not found"
    else:
      data = response.json()
      name = data["name"]
      blog = data["blog"]
      public_repo = data["public_repos"]
      location = data["location"]
      followers = data["followers"]
      email = data["email"]
      company = data["company"]
      login_name = data["login"]
      hire = data["hireable"]
      avatar = data["avatar_url"]
      return render_template("result.html",name=name , blog=blog, followers=followers,email=email , company=company,login=login_name , hire=hire , location=location , public_repo=public_repo , avatar=avatar)




app.run(host="0.0.0.0",debug=True)
