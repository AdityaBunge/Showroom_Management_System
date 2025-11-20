# Showroom Management System

This project is a showroom management system for cars built using Django. It provides functionalities for managing cars, customers, sales, and inventory.

## Features

- Manage car listings
- Handle customer information
- Process sales transactions
- Track inventory

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd showroom-management
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Set up environment variables by copying `.env.example` to `.env` and updating the values as necessary.

## Usage

1. Run database migrations:
   ```
   python manage.py migrate
   ```

2. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

3. Start the development server:
   ```
   python manage.py runserver
   ```

4. Access the application at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.