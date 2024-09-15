<h1 align="center">CORSINATOR</h1>

<div align="center">
<a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/framework-flask-green" height="20"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/language-python-blue" height="20"></a>
</div>

Corsinator is a simple Flask-based proxy server designed to handle Cross-Origin Resource Sharing (CORS) issues by forwarding HTTP requests to a target API. It supports `GET`, `POST`, `PUT`, and `DELETE` methods and handles CORS headers to facilitate cross-origin interactions.

## Features

- Forwards requests to a specified target API.
- Supports `GET`, `POST`, `PUT`, and `DELETE` HTTP methods.
- Configurable target API URL.
- Automatically sets CORS headers to allow cross-origin requests.

## Prerequisites

- Python 3.x
- Flask (`pip install flask`)
- Requests library (`pip install requests`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/corsinator.git
   cd corsinator
   ```

2. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

   **`requirements.txt` should contain:**

   ```
   Flask==2.3.2
   requests==2.28.2
   ```

3. **Configure the target URL:**

   Edit the `TARGET_URL` variable in `main.py` to point to your target API:

   ```python
   TARGET_URL = 'https://api.example.com/api/v1'
   ```

4. **Run the Corsinator server:**

   ```bash
   python main.py
   ```

   The server will start on `http://localhost:8080`.

## Integration with a React Project

To integrate Corsinator with your React application, follow these steps:

1. **Configure the React application to use the proxy:**

   In your React project's root directory, open (or create) `package.json` and add a `proxy` field to point to the Corsinator server:

   ```json
   {
     "name": "your-react-app",
     "version": "1.0.0",
     "private": true,
     "proxy": "http://localhost:8080",
     "dependencies": {
       ...
     },
     ...
   }
   ```

2. **Make API requests from your React app:**

   In your React components or services, you can make API requests without specifying the full URL. For example:

   ```javascript
   // In a React component or service file
   import axios from "axios";

   const fetchData = async () => {
     try {
       const response = await axios.get("/some-endpoint");
       console.log(response.data);
     } catch (error) {
       console.error("Error fetching data:", error);
     }
   };

   fetchData();
   ```

   The proxy configuration in `package.json` will forward the request to `http://localhost:8080/some-endpoint`, where it will be handled by Corsinator.

## Testing

You can test the Corsinator server using tools like `curl` or Postman, or by making API requests from your React application.

## Troubleshooting

- Ensure the Corsinator server is running before making requests from the React app.
- Verify that the target URL is correctly configured in `main.py`.
- Check console logs and network activity for errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
