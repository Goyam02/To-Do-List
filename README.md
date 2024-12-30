# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows you to view, add, mark as complete, and delete tasks. The tasks are saved in a JSON file, and a backup of the tasks file is created before exiting the application.

## Features

- View tasks
- Add a new task
- Mark a task as complete
- Delete a task
- Backup tasks file

## Requirements

- Python 3.x
- `emoji` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Goyam02/TO-DO-List.git
    cd TO-DO-List
    ```

2. Install the required library:

    ```sh
    pip install emoji
    ```

## Usage

Run the application:

```sh
python to_do_list.py

Follow the on-screen instructions to manage your tasks.

File Structure
to_do_list.py: Main script containing the To-Do List application logic.
Data/tasks.json: JSON file where tasks are stored.
Functions
load_tasks(): Loads tasks from the JSON file.
save_tasks(): Saves tasks to the JSON file.
backup_file(): Creates a backup of the tasks file.
clear_console(): Clears the console screen.
show_Menu(): Displays the main menu.
view_task(): Displays the list of tasks.
add_task(): Adds a new task to the list.
complete_task(): Marks a task as complete.
delete_task(): Deletes a task from the list.
main(): Main function to run the application.
```

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Goyam02/To-Do-List/blob/main/LICENSE) file for details.


## Contributing
```sh
Contributions are welcome! Please open an issue or submit a pull request for any changes.
```
## Author
```sh
GOYAM JAIN
