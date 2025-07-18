# Web Scientific Calculator

A modern, feature-rich scientific calculator built with HTML, CSS, and vanilla JavaScript. This project provides a clean, user-friendly interface with both basic and advanced mathematical functions.

![Calculator Screenshot](httpss://i.imgur.com/YOUR_SCREENSHOT_URL.png) 
*(Note: You can replace the above URL with a real screenshot of the calculator)*

## Features

*   **Standard Arithmetic:** Addition, Subtraction, Multiplication, Division.
*   **Scientific Functions:**
    *   Trigonometric: `sin`, `cos`, `tan`
    *   Logarithmic: `log` (base 10), `ln` (natural log)
    *   Exponents & Roots: `x^y`, `√` (square root)
*   **Order of Operations:** Support for parentheses `()` to group expressions.
*   **Mathematical Constants:**
    *   `π` (Pi)
    *   `e` (Euler's number)
*   **Memory Functions:**
    *   `MC`: Memory Clear
    *   `MR`: Memory Recall
    *   `M+`: Memory Add
    *   `M-`: Memory Subtract
*   **Calculation History:**
    *   View a list of your recent calculations.
    *   Option to clear the history.
*   **Modern & Responsive UI:**
    *   A clean, neumorphic design.
    *   A separate panel for history for a better user experience.
    *   Backspace and Clear (`C`) functionality.

## How to Use

There are two ways to run the calculator:

### 1. Simple (Directly Opening the File)

1.  Ensure you have all three files (`index.html`, `style.css`, `script.js`) in the same directory.
2.  Open the `index.html` file directly in your web browser (e.g., Chrome, Firefox, Edge).

### 2. Recommended (Using a Local Server)

For the best experience and to avoid any potential browser security issues with local files, it's recommended to serve the files using a simple local web server.

1.  Open your terminal or command prompt in the project directory.
2.  Run the following command (you need Python installed):
    ```bash
    python3 -m http.server
    ```
    If you have Python 2, you might need to use `python -m SimpleHTTPServer`.
3.  Open your web browser and navigate to `http://localhost:8000`.

## File Structure

*   `index.html`: The main HTML file containing the structure of the calculator and history panel.
*   `style.css`: The CSS file for all styling, including the layout, buttons, and neumorphic design.
*   `script.js`: The JavaScript file that contains all the logic for calculations, history, and memory functions.
