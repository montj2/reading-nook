# Contributing to Reading Nook

We welcome contributions from everyone! Whether you're fixing a bug, adding a new feature, or improving the documentation, your help is greatly appreciated.

## How to Contribute

1.  **Fork the repository:** Click the "Fork" button on the top right corner of the repository page. This will create a copy of the repository under your GitHub account.

2.  **Clone your fork:**

    ```bash
    git clone [https://github.com/](https://github.com/)<your_username>/reading-nook.git
    ```

3.  **Create a new branch:**

    ```bash
    git checkout -b my-feature-branch
    ```

4.  **Make your changes:** 

    *   Follow the coding style guidelines (see below).
    *   Write tests for any new code you add.
    *   Ensure that your changes don't break existing functionality.

5.  **Commit your changes:**

    ```bash
    git add .
    git commit -m "Add my new feature"
    ```

6.  **Push to your fork:**

    ```bash
    git push origin my-feature-branch
    ```

7.  **Open a pull request:** Go to the original repository and click the "New pull request" button. Select your fork and branch, and provide a clear description of your changes.

## Coding Style

*   We follow the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) for Python code.
*   Use descriptive variable and function names.
*   Write clear and concise comments.

## Testing

*   We use `pytest` for testing.
*   All new code should have corresponding tests.
*   Run tests before submitting a pull request:

    ```bash
    tox
    ```

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We follow the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

If you have any questions, please feel free to open an issue or reach out to the maintainers.

Thank you for your contributions!

