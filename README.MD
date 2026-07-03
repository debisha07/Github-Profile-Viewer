# GitHub Profile Dashboard

A Flask-based web application that allows users to search for GitHub profiles and view public account information using the GitHub REST API.

## Features

* Search any GitHub username
* View profile avatar
* Display name and username
* View follower count
* View public repository count
* View company and location information
* View blog/website links
* Responsive web interface using Flask templates
* Real-time data fetched from the GitHub API

## Technologies Used

* Python
* Flask
* HTML
* CSS
* GitHub REST API
* Requests Library

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── templates
│   ├── index.html
│   └── result.html
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd github-profile-dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:5000
```

## How It Works

1. User enters a GitHub username.
2. Flask receives the request.
3. The application sends a request to the GitHub API.
4. Profile data is retrieved and processed.
5. Results are displayed in a user-friendly dashboard.

## Future Improvements

* Display top repositories
* Show most-used programming language
* Display account age
* Docker support
* GitHub Actions CI/CD pipeline
* Improved UI and error handling
* User statistics and insights

## Learning Outcomes

This project helped practice:

* Flask web development
* API integration
* JSON data handling
* Template rendering with Jinja2
* HTTP requests using Python Requests
* Basic DevOps concepts and containerization

## License

This project is intended for learning and educational purposes.
