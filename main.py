import tkinter as tk
import csv

def convert_to_csv():
    log_file = log_file_entry.get()
    csv_file = csv_file_entry.get()

    with open(log_file, 'r') as f:
        data = f.readlines()

    rows = []
    for line in data:
        # Handle potential errors in data structure
        try:
            fields = line.split(" ")
            tuple_data = {}
            for field in fields:
                key, value = field.split("=", 1)
                tuple_data[key.strip()] = value.strip('"')  # Remove enclosing quotes
            rows.append(tuple_data)
        except ValueError:
            print(f"Error parsing line: {line}")

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=tuple_data.keys())
        writer.writeheader()
        writer.writerows(rows)

    result_label.config(text="Conversion completed successfully!")

# Create the GUI window
window = tk.Tk()
window.title("Log to CSV Converter")

# Create input fields for log and CSV file paths
log_file_label = tk.Label(window, text="Log File:")
log_file_label.pack()
log_file_entry = tk.Entry(window)
log_file_entry.pack()

csv_file_label = tk.Label(window, text="CSV File:")
csv_file_label.pack()
csv_file_entry = tk.Entry(window)
csv_file_entry.pack()

# Create a button to trigger the conversion
convert_button = tk.Button(window, text="Convert", command=convert_to_csv)
convert_button.pack()

# Create a label to display the conversion result
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
