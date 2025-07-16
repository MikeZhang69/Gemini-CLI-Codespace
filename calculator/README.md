# Finance Calculator Suite

This folder contains a Python-based finance calculator app with a modern GUI, including:

- **NPV Calculator**: Calculate Net Present Value for investment projects.
- **Standard Calculator**: Basic arithmetic calculator (iPhone style).

## Features
- User-friendly GUI (tkinter)
- Modular code for easy extension
- Accurate financial calculations

## How to Run
1. Make sure you have Python 3 installed.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```

> **Note:**
> If running in a remote or headless environment (e.g., VS Code devcontainer), you need X11 forwarding to display the GUI. For local use, just run as above.

## File Structure
- `app.py` — Main GUI application
- `financial_calculator.py` — Financial calculation logic (NPV, etc.)
- `requirements.txt` — Python dependencies

## Extending
You can add more calculators or financial tools by extending `financial_calculator.py` and updating the GUI in `app.py`.

---

© 2025 Your Name or Company
