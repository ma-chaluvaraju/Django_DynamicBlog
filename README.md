# Dynamic_Blog

A dynamic blog application is a website that allows users to interact with content in real-time. Unlike a static blog where the content remains fixed, a dynamic blog can adapt and update its content based on user interactions, data from a database, or external sources. It is Built using the Django and it various features, HTML and CSS and Bootstrap for better user interface

## Features

- User Interaction: Allows user registration, login, comments
- Content Management: Enables admins or authors to create, edit, delete, and publish blog posts, with content stored in a database.
- Search & Filtering: Provides search functionality, categories to filter and sort blog posts based on user preferences.

## Getting Started

### Prerequisites

- Docker

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/ma-chaluvaraju/Django_DynamicBlog.git
    cd Django_DynamicBlog
    ```

2. Build and run the Docker container:

    ```sh
    docker build -t <image-name> .
    docker run --name Blog -d -p 5002:5000 <image-name>
    ```

3. Open your browser and navigate to `http://localhost:5002`.

### API Endpoints

- `GET /`: Displays the homepage with featured or latest blog posts.
- `GET /category/`: Lists all available blog categories.
- `GET /category/<category_name>/`: Lists blog posts filtered by category.
- `GET /blogs/<slug:slug>/`: Displays a specific blog post based on its slug.
- `POST /blog/search/`: Accepts a search query and returns relevant blog posts.
- `POST /register/`: Registers a new user with details (username, email, password).
- `POST /login/`: Authenticates a user based on login credentials (username/email and password).
- `POST /logout/`: Logs out the currently authenticated user.
- `GET /dashboard/`: Displays the user’s dashboard with personal data, blog posts, and interactions.
- `GET /admin/`: Admin interface to manage users, posts, and comments (typically served via Django's admin panel).
  
### Technologies Used

- Django
- Django-crispy-forms
- Pillow
- Bootstrap
- Docker
- HTML
- CSS

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Contact

For any inquiries, please contact [machaluvaraju147@gmail.com](mailto:machaluvaraju147@gmail.com).