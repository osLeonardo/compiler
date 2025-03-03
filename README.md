# Compiler Project

This project is a simple compiler that processes a custom programming language. It includes lexical, syntactic, and semantic analysis components to parse and validate the source code.

## Contributors
- João Vitor Alves
- Leonardo Spilere

## Project Structure

- `main.py`: The main entry point of the compiler.
- `service/lexico.py`: Contains the lexical analyzer.
- `service/sintatico.py`: Contains the syntactic analyzer.
- `service/simbolos.py`: Contains the symbol table implementation.
- `data/content/`: Directory containing example source code files.

## How to Run

1. Clone the repository using HTTPS or SSH:
  ```sh
  # Using HTTPS
  git clone https://github.com/osLeonardo/compiler.git
  # Using SSH
  git clone git@github.com:osLeonardo/compiler.git
  ```

2. Ensure you have Python installed. You can download and install Python from [python.org](https://www.python.org/). Verify the installation by checking the version:
  ```sh
  python --version
  ```

3. Install the required dependencies:
  ```sh
  pip install numpy
  ```

4. Navigate to the project directory and run the compiler:
  ```sh
  cd compiler
  python main.py
  ```

5. Follow the on-screen menu to select the source code file you want to process.
