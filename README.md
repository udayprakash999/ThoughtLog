```markdown
# Journal App

A simple and elegant journal app built with Python using Tkinter. This app allows users to manage their personal journal entries by providing options to add, edit, delete, view, and store them. All journal entries are stored in a JSON file, ensuring data persistence.

## Features

- **Add New Entry**: Write new journal entries with titles, moods, and text.
- **Edit Entries**: Modify the title, mood, or text of existing journal entries.
- **Delete Entries**: Remove journal entries from the list.
- **View Entries**: View the full details of a selected journal entry.
- **List All Entries**: View a list of all journal entries with titles and dates.
- **Persistent Storage**: Journal entries are stored in a JSON file (`journal_entries.json`).

## Requirements

- Python 3.x
- Tkinter (usually included with Python, no separate installation required)

## Installation

To run this app locally, follow these steps:

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/journal-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd journal-app
   ```

3. Make sure you have Python installed. You can verify this with:
   ```bash
   python --version
   ```

4. Tkinter should be pre-installed with Python. If you encounter any issues with Tkinter, refer to the [official installation guide](https://tkdocs.com/tutorial/install.html).

5. To run the app, simply execute:
   ```
   python main.py
   ```

## Usage

1. **Add New Entry**: Enter a title, mood (optional), and journal text, then click **"Add Entry"**.
   
2. **Edit Entry**: Select an entry from the list, modify the content, and click **"Edit Selected Entry"**.
   
3. **Delete Entry**: Select an entry and click **"Delete Selected Entry"**.
   
4. **View Entry**: Select an entry to view its full details in a pop-up window.

## Data Storage

The journal entries are saved in `journal_entries.json`. This file stores each entry's:

- `title`: The title of the journal entry.
- `mood`: An optional mood or tag associated with the entry.
- `text`: The main content of the journal entry.
- `date`: The timestamp when the entry was added or last edited.
