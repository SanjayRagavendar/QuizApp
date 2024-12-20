# QuizApp

QuizApp is a dynamic and interactive web application designed to test users' knowledge on various topics through engaging quizzes. Built using modern web development technologies, this project is ideal for both learning and entertainment purposes.

## Features

- **User-friendly Interface**: A clean and intuitive interface for seamless user interaction.
- **Multiple Quiz Categories**: Choose from a variety of topics to test your knowledge.
- **Timed Quizzes**: Challenge yourself with time-bound questions.
- **Scoring System**: Keep track of your performance with real-time scoring.
- **Responsive Design**: Accessible on desktops, tablets, and smartphones.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Version Control**: Git and GitHub

## Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SanjayRagavendar/QuizApp.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd QuizApp
   ```

3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the Database**:
   ```bash
   python
   >>> from models import db
   >>> db.create_all()
   >>> exit()
   ```

6. **Start the Application**:
   ```bash
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

1. Open the application in your browser.
2. Register a new user or log in.
3. Admins can create new quizzes via the `/quiz_create` route.
4. Users can view quizzes on the dashboard, attempt them, and submit answers.
5. Results can be viewed on the `/result` page.

### Notes

- The `admin_required` decorator restricts certain routes to admins.
- JWT authentication is used for secure user login and session handling.

## Future Enhancements

- Add user feedback for quizzes.
- Support multiple question types (e.g., short answers, true/false).
- Add detailed result analysis with explanations.
- Enhance UI for better user experience.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.
