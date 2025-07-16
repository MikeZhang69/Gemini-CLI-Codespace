import tkinter as tk
from tkinter import messagebox
from financial_calculator import calculate_npv

def open_npv_calculator():
    npv_window = tk.Toplevel()
    npv_window.title("NPV Calculator")
    npv_window.geometry("350x300")

    tk.Label(npv_window, text="Initial Investment (negative for outflow):").pack(pady=5)
    initial_entry = tk.Entry(npv_window)
    initial_entry.pack(pady=5)

    tk.Label(npv_window, text="Cash Flows (comma-separated):").pack(pady=5)
    cash_flows_entry = tk.Entry(npv_window)
    cash_flows_entry.pack(pady=5)

    tk.Label(npv_window, text="Discount Rate (%):").pack(pady=5)
    discount_entry = tk.Entry(npv_window)
    discount_entry.pack(pady=5)

    result_label = tk.Label(npv_window, text="")
    result_label.pack(pady=10)

    def calculate():
        try:
            initial = float(initial_entry.get())
            cash_flows = [float(x.strip()) for x in cash_flows_entry.get().split(',') if x.strip()]
            discount = float(discount_entry.get())
            npv = calculate_npv(initial, cash_flows, discount)
            result_label.config(text=f"NPV: {npv:.2f}")
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    tk.Button(npv_window, text="Calculate NPV", command=calculate).pack(pady=10)
def open_standard_calculator():
    calc_window = tk.Toplevel()
    calc_window.title("Standard Calculator")
    calc_window.geometry("320x480")

    # Display
    display_var = tk.StringVar(value="0")
    display = tk.Entry(calc_window, textvariable=display_var, font=("Arial", 28), bd=10, relief=tk.RIDGE, justify='right', state='readonly', readonlybackground='white')
    display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

    # Calculator state
    calc_state = {"current": "0", "operator": None, "operand": None, "reset": False}

    def input_digit(d):
        if calc_state["reset"] or display_var.get() == "0":
            display_var.set(d)
            calc_state["reset"] = False
        else:
            display_var.set(display_var.get() + d)
    def input_dot():
        if "." not in display_var.get():
            display_var.set(display_var.get() + ".")
    def clear():
        display_var.set("0")
        calc_state["operator"] = None
        calc_state["operand"] = None
        calc_state["reset"] = False
    def plus_minus():
        val = display_var.get()
        if val.startswith("-"):
            display_var.set(val[1:])
        elif val != "0":
            display_var.set("-" + val)
    def percent():
        try:
            display_var.set(str(float(display_var.get()) / 100))
        except Exception:
            display_var.set("Error")
    def set_operator(op):
        try:
            calc_state["operand"] = float(display_var.get())
            calc_state["operator"] = op
            calc_state["reset"] = True
        except Exception:
            display_var.set("Error")
    def calculate():
        try:
            if calc_state["operator"] and calc_state["operand"] is not None:
                a = calc_state["operand"]
                b = float(display_var.get())
                op = calc_state["operator"]
                if op == "+":
                    result = a + b
                elif op == "-":
                    result = a - b
                elif op == "×":
                    result = a * b
                elif op == "÷":
                    if b == 0:
                        display_var.set("Error")
                        return
                    result = a / b
                else:
                    result = b
                display_var.set(str(result).rstrip("0").rstrip(".") if "." in str(result) else str(result))
                calc_state["operator"] = None
                calc_state["operand"] = None
                calc_state["reset"] = True
        except Exception:
            display_var.set("Error")

    # Button layout (iPhone style)
    buttons = [
        [ ("C", clear), ("+/-", plus_minus), ("%", percent), ("÷", lambda: set_operator("÷")) ],
        [ ("7", lambda: input_digit("7")), ("8", lambda: input_digit("8")), ("9", lambda: input_digit("9")), ("×", lambda: set_operator("×")) ],
        [ ("4", lambda: input_digit("4")), ("5", lambda: input_digit("5")), ("6", lambda: input_digit("6")), ("-", lambda: set_operator("-")) ],
        [ ("1", lambda: input_digit("1")), ("2", lambda: input_digit("2")), ("3", lambda: input_digit("3")), ("+", lambda: set_operator("+")) ],
        [ ("0", lambda: input_digit("0")), (".", input_dot), ("=", calculate) ]
    ]
    for r, row in enumerate(buttons):
        for c, (text, cmd) in enumerate(row):
            colspan = 2 if text == "0" and r == 4 and c == 0 else 1
            btn = tk.Button(calc_window, text=text, width=5 if colspan==1 else 12, height=2, font=("Arial", 18), command=cmd)
            btn.grid(row=r+1, column=c, columnspan=colspan, padx=4, pady=4, sticky="nsew")
            if colspan == 2:
                break
    # Make grid cells expand
    for i in range(5):
        calc_window.grid_rowconfigure(i, weight=1)
    for i in range(4):
        calc_window.grid_columnconfigure(i, weight=1)


def main():
    root = tk.Tk()
    root.title("Finance Calculator")
    root.geometry("300x250")

    tk.Label(root, text="Finance Calculator", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="NPV Calculator", width=20, command=open_npv_calculator).pack(pady=10)
    tk.Button(root, text="Standard Calculator", width=20, command=open_standard_calculator).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
