import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ThoughtLog")
        self.root.geometry("600x500")

        self.bg_color = "#2C3E50"
        self.button_color = "#3498DB"
        self.fg_color = "#F0F0F0"
        self.entry_bg = "#ECF0F1"
        self.dark_text_color = "#2C3E50"

        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        self.listbox_font = ("Arial", 11)

        self.load_entries()

        self.paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL, bg=self.bg_color)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(self.paned_window, padx=10, pady=10, bg=self.bg_color)
        self.paned_window.add(self.left_frame)

        self.right_frame = tk.Frame(self.paned_window, padx=10, pady=10, bg=self.bg_color)
        self.paned_window.add(self.right_frame)

        self.create_left_frame_widgets()
        self.create_right_frame_widgets()

    def create_left_frame_widgets(self):
        self.entry_title_label = tk.Label(self.left_frame, text="Entry Title:", fg=self.fg_color, bg=self.bg_color, font=self.label_font)
        self.entry_title_label.pack(pady=5)
        self.entry_title = tk.Entry(self.left_frame, width=40, bg=self.entry_bg, fg=self.dark_text_color, font=self.entry_font)
        self.entry_title.pack(pady=5)

        self.entry_mood_label = tk.Label(self.left_frame, text="Mood (Tag):", fg=self.fg_color, bg=self.bg_color, font=self.label_font)
        self.entry_mood_label.pack(pady=5)
        self.entry_mood = tk.Entry(self.left_frame, width=40, bg=self.entry_bg, fg=self.dark_text_color, font=self.entry_font)
        self.entry_mood.pack(pady=5)

        self.entry_text_label = tk.Label(self.left_frame, text="Your Entry:", fg=self.fg_color, bg=self.bg_color, font=self.label_font)
        self.entry_text_label.pack(pady=5)
        self.entry_text = tk.Text(self.left_frame, height=10, width=40, bg=self.entry_bg, fg=self.dark_text_color, font=self.entry_font)
        self.entry_text.pack(pady=10)

        self.add_button = tk.Button(self.left_frame, text="Add Entry", command=self.add_entry, bg=self.button_color, fg=self.fg_color, font=self.button_font)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.left_frame, text="Edit Selected Entry", command=self.edit_entry, bg=self.button_color, fg=self.fg_color, font=self.button_font)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.left_frame, text="Delete Selected Entry", command=self.delete_entry, bg=self.button_color, fg=self.fg_color, font=self.button_font)
        self.delete_button.pack(pady=5)

        self.view_button = tk.Button(self.left_frame, text="View Selected Entry", command=self.view_entry, bg=self.button_color, fg=self.fg_color, font=self.button_font)
        self.view_button.pack(pady=5)

    def create_right_frame_widgets(self):
        self.entries_listbox_label = tk.Label(self.right_frame, text="Entries:", fg=self.fg_color, bg=self.bg_color, font=self.label_font)
        self.entries_listbox_label.pack(pady=10)

        self.entries_listbox = tk.Listbox(self.right_frame, width=40, height=15, bg=self.entry_bg, fg=self.dark_text_color, font=self.listbox_font)
        self.entries_listbox.pack(side=tk.LEFT, pady=10, padx=5)

        self.scrollbar = tk.Scrollbar(self.right_frame, orient=tk.VERTICAL, command=self.entries_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.entries_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entries_listbox.bind("<<ListboxSelect>>", self.load_selected_entry)

        self.update_entries_listbox()

    def load_entries(self):
        try:
            with open("journal_entries.json", "r") as file:
                self.entries = json.load(file)
        except FileNotFoundError:
            self.entries = []

    def save_entries(self):
        with open("journal_entries.json", "w") as file:
            json.dump(self.entries, file, indent=4)

    def add_entry(self):
        title = self.entry_title.get()
        mood = self.entry_mood.get()
        text = self.entry_text.get("1.0", tk.END).strip()

        if not title or not text:
            messagebox.showwarning("Input Error", "Please enter both title and text for the entry.")
            return

        entry = {
            "title": title,
            "mood": mood,
            "text": text,
            "date": str(datetime.now())
        }
        self.entries.append(entry)
        self.save_entries()
        self.update_entries_listbox()
        self.clear_entries()

    def edit_entry(self):
        selected = self.entries_listbox.curselection()
        if selected:
            index = selected[0]
            entry = self.entries[index]

            title = self.entry_title.get()
            mood = self.entry_mood.get()
            text = self.entry_text.get("1.0", tk.END).strip()

            if not title or not text:
                messagebox.showwarning("Input Error", "Please enter both title and text for the entry.")
                return

            self.entries[index] = {
                "title": title,
                "mood": mood,
                "text": text,
                "date": str(datetime.now())
            }

            self.save_entries()
            self.update_entries_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Please select an entry to edit.")

    def delete_entry(self):
        selected = self.entries_listbox.curselection()
        if selected:
            index = selected[0]
            del self.entries[index]
            self.save_entries()
            self.update_entries_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select an entry to delete.")

    def view_entry(self):
        selected = self.entries_listbox.curselection()
        if selected:
            index = selected[0]
            entry = self.entries[index]
            entry_details = f"Title: {entry['title']}\nMood: {entry['mood']}\nDate: {entry['date']}\n\n{entry['text']}"
            messagebox.showinfo("View Entry", entry_details)
        else:
            messagebox.showwarning("Selection Error", "Please select an entry to view.")

    def load_selected_entry(self, event):
        selected = self.entries_listbox.curselection()
        if selected:
            index = selected[0]
            entry = self.entries[index]
            self.entry_title.delete(0, tk.END)
            self.entry_title.insert(0, entry["title"])
            self.entry_mood.delete(0, tk.END)
            self.entry_mood.insert(0, entry["mood"])
            self.entry_text.delete("1.0", tk.END)
            self.entry_text.insert("1.0", entry["text"])

    def update_entries_listbox(self):
        self.entries_listbox.delete(0, tk.END)
        for entry in self.entries:
            display_text = f"{entry['title']} ({entry['date']})"
            self.entries_listbox.insert(tk.END, display_text)

    def clear_entries(self):
        self.entry_title.delete(0, tk.END)
        self.entry_mood.delete(0, tk.END)
        self.entry_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()
