# Reading Nook

A self-hosted, open-source "read it later" service built with Flask.

## Features (Planned)

*   Save articles from anywhere on the web.
*   Read saved articles offline.
*   Organize articles with tags and folders.
*   Sync your reading list across multiple devices.
*   ... and more!

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/](https://github.com/)<your_username>/reading-nook.git
    ```

2.  **Install dependencies:**

    ```bash
    cd reading-nook
    poetry install
    ```

3.  **Set up the database:**

    *   Create a database (e.g., PostgreSQL, SQLite).
    *   Update the database configuration in `app/config.py`.
    *   Run database migrations:

    ```bash
    poetry run flask db upgrade
    ```

4.  **Run the development server:**

    ```bash
    poetry run flask run
    ```

5.  **Open your browser and visit http://127.0.0.1:5000**

## Contributing

We welcome contributions from the community! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to get involved.

## License

This project is licensed under the ISC License. See the [LICENSE](LICENSE) file for details.

