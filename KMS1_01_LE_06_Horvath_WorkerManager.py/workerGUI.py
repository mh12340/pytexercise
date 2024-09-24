import tkinter as tk    #import the tkinter library for GUI
from tkinter import messagebox, simpledialog, ttk   #import necessary tkinter components
from worker_utils import (first_name_check, last_name_check, position_check, birthday_check, phone_number_check,
                          email_check, calculate_days)  #import validation and calculation functions from worker_utils

class WorkerManagerApp:     #define the main class for the worker manager application
    def __init__(self, root):
        self.root = root    #assign the root window to an instance variable
        self.root.title("Worker Manager")   #set the title of the window
        self.load_worker_infos()  #load worker infos at startup
        self.create_widgets()   #create the GUI widgets
        #define buttons for various actions in the application
        self.add_worker_button = tk.Button(self.root, text="Add Worker", command=self.add_worker)
        self.show_list_button = tk.Button(self.root, text="Show Unfiltered Worker List", command=self.show_worker_list)
        self.show_filtered_list_button = tk.Button(self.root, text="Show Filtered Worker List",
                                                   command=self.show_filtered_list)
        self.filter_button = tk.Button(self.root, text="Filter Workers", command=self.filter_workers)
        self.edit_worker_button = tk.Button(self.root, text="Edit Worker", command=self.edit_worker)
        self.filter_export_button = tk.Button(self.root, text="Filter by Birth Month and Export",
                                              command=self.filter_export)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)

    def create_widgets(self):
        #label to show title at the top
        tk.Label(self.root, text="Worker Manager", font=("Arial", 16)).pack(pady=10)

        #create buttons for different actions and pack them into the window

        self.add_worker_button = tk.Button(self.root, text="Add Worker", command=self.add_worker)
        self.add_worker_button.pack(pady=5)

        self.show_list_button = tk.Button(self.root, text="Show Unfiltered Worker List", command=self.show_worker_list)
        self.show_list_button.pack(pady=5)

        self.show_filtered_list_button = tk.Button(self.root, text="Show Filtered Worker List",
                                                   command=self.show_filtered_list)
        self.show_filtered_list_button.pack(pady=5)

        self.filter_button = tk.Button(self.root, text="Filter Workers", command=self.filter_workers)
        self.filter_button.pack(pady=5)

        self.edit_worker_button = tk.Button(self.root, text="Edit Worker", command=self.edit_worker)
        self.edit_worker_button.pack(pady=5)

        self.filter_export_button = tk.Button(self.root, text="Filter by Birth Month and Export",
                                              command=self.filter_export)
        self.filter_export_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def load_worker_infos(self):
        #load worker info from 'txt1.txt'
        try:
            with open('txt1.txt', 'r') as file:
                lines = file.readlines()    #read all lines from the file

            global worker_infos     #declare worker_infos as a global variable
            worker_infos = [tuple(line.strip().split(', ')) for line in lines]

        except FileNotFoundError:
            worker_infos = []   #if file doesnt exist, initialize an empty list

    def add_worker(self):
        #opens a new window to collect worker info
        self.collect_worker_gui()

    def show_worker_list(self):
        self.load_worker_infos()  #reload worker_infos to ensure it's up-to-date
        self.show_list_gui(worker_infos)

    def show_filtered_list(self):
        try:
            #attempt to read the filtered worker list from 'txt2.txt'
            with open('txt2.txt', 'r') as file:
                lines = file.readlines()

            #check if any data was read from the file
            if not lines:
                messagebox.showinfo("Info", "No filtered workers found.")
                return

            #prepare the list of workers to be displayed
            filtered_workers = [line.strip().split(', ') for line in lines]

            #show the filtered workers in a new Tkinter window
            self.show_list_gui(filtered_workers)

        except FileNotFoundError:
            messagebox.showerror("Error", "No filtered list found. Please filter first.")
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying filtered workers: {str(e)}")

    def filter_workers(self):
        self.load_worker_infos()  #reload worker_infos to ensure it's up-to-date

        if not worker_infos:
            messagebox.showinfo("Info", "No workers available to filter.")
            return

        #create a new window for filter input
        filter_window = tk.Toplevel(self.root)  #create new top level window
        filter_window.title("Filter Workers")   #set title of the filter window

        tk.Label(filter_window, text="Enter the value to filter by:").pack(pady=5)  #label for input
        filter_entry = tk.Entry(filter_window)      #entry field for user input
        filter_entry.pack(pady=5)   #pack the entry field

        def apply_filter():
            search_term = filter_entry.get().strip().lower()    #get input and convert to lowercase
            #filter worker_infos based on search_term
            filtered_infos = [worker for worker in worker_infos if
                              any(search_term in str(field).lower() for field in worker)]

            if filtered_infos:
                self.show_list_gui(filtered_infos)  #show filtered workers
                with open('txt2.txt', 'w') as file: #write filtered workers to 'txt2.txt'
                    for worker in filtered_infos:
                        file.write(', '.join(worker) + '\n')
                messagebox.showinfo("Success", "Filtered workers exported to txt2.txt") #show success message
            else:
                messagebox.showinfo("Info", "No workers match the given filter.")   #no match message

            filter_window.destroy() #close the filter window

        tk.Button(filter_window, text="Apply Filter", command=apply_filter).pack(pady=10)   #button to apply filter

    def edit_worker(self):
        self.load_worker_infos()  #reload worker_infos to ensure it's up-to-date

        if not worker_infos:
            messagebox.showinfo("Info", "No workers available to edit.")
            return

        #open a new window to select a worker to edit
        select_window = tk.Toplevel(self.root)
        select_window.title("Select Worker to Edit")

        for i, worker in enumerate(worker_infos):
            #create a button for each worker
            tk.Button(select_window, text=f"{i + 1}. {worker[0]} - {worker[1]}",
                      command=lambda i=i: self.open_edit_window(i)).pack(pady=2) #open edit window for selected worker

    def open_edit_window(self, worker_index):
        #open a new window to edit worker information
        worker = worker_infos[worker_index] #get the worker info to edit
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit {worker[0]}")  #set the title of the edit window

        fields = ["Name", "Position", "Address", "Birthday", "Phone", "Email"]  #field names
        entries = []    #list to store entry fields

        for i, field in enumerate(fields):
            tk.Label(edit_window, text=f"{field}:").grid(row=i, column=0, padx=5, pady=5)   #label for each field
            entry = tk.Entry(edit_window)   #create an entry field
            entry.insert(0, worker[i])  #pre-fill entry with current worker info
            entry.grid(row=i, column=1, padx=5, pady=5) #place entry field in the grid
            entries.append(entry)   #add the entry to the list

        def save_changes():
            #get new values from entry fields
            new_values = [entry.get() for entry in entries]
            worker_infos[worker_index] = tuple(new_values)  #update the global worker_infos list
            #update the txt1.txt file with the edited information
            with open('txt1.txt', 'w') as file:
                for worker in worker_infos:
                    file.write(', '.join(worker) + '\n')
            messagebox.showinfo("Success", "Worker info updated.")  #show success message
            edit_window.destroy()   #close the edit window

        #button to save changes
        tk.Button(edit_window, text="Save Changes", command=save_changes).grid(row=len(fields), column=0, columnspan=2,
                                                                               pady=10)

    def filter_export(self):
        self.load_worker_infos()  # reload worker_infos to ensure it's up-to-date

        if not worker_infos:  # check if there are workers to filter
            messagebox.showinfo("Info", "No workers available to filter and export.")
            return

        try:
            # ask for the birth month using a pop-up dialog
            month = simpledialog.askstring("Filter by Birth Month", "Enter the birth month (1-12):")
            if not month:
                messagebox.showinfo("Info", "No month was entered.")
                return

            #validate month input
            if not month.isdigit() or not (1 <= int(month) <= 12):
                messagebox.showerror("Input Error", "Invalid month. Please enter a number between 1 and 12.")
                return

            # filter workers based on the birth month
            filtered_workers = [
                worker for worker in worker_infos
                if worker[3].split('.')[1] == month.zfill(2)
            ]

            # write the filtered workers to 'filtered_bday.txt'
            with open('filtered_bday.txt', 'w') as file:
                for worker in filtered_workers:
                    file.write(', '.join(worker) + '\n')

            # show the filtered workers in a new Tkinter window
            if filtered_workers:
                self.show_list_gui(filtered_workers)
                messagebox.showinfo("Success", "Workers filtered by birth month and exported successfully.")    #success message
            else:
                messagebox.showinfo("Info", "No workers matched the birth month.") #no matches message

        except Exception as e:
            messagebox.showerror("Error", f"Error filtering and exporting: {str(e)}")   #catch and report any errors

    def show_list_gui(self, workers):
        #open a new window to display the worker list
        if not workers:
            messagebox.showinfo("Info", "No worker information available.") #handle empty list
            return

        # create a new top level window to display the worker list
        list_window = tk.Toplevel(self.root)
        list_window.title("Worker List")    #set the title of the list window

        # define the column headers for the list
        headers = ["First & Last Name", "Position", "Address", "Birthday", "Phone Number", "Email",
                   "Days Since Last Birthday", "Days Until Next Birthday"]
        columns = ["name", "position", "address", "birthday", "phone", "email", "days_since_birthday",
                   "days_until_birthday"]

        # create a treeview widget for displaying the list in a table format
        tree = ttk.Treeview(list_window, columns=columns, show="headings")
        for col, heading in zip(columns, headers):
            tree.heading(col, text=heading) #set each column heading
            tree.column(col, width=150) #set column width

        # insert the worker data into the treeview
        for worker in workers:
            # calculate the days since and until the next birthday
            days_since_birthday, days_until_birthday = calculate_days(worker[3])
            tree.insert("", "end", values=list(worker) + [days_since_birthday, days_until_birthday])    #add worker info

        tree.pack(fill="both", expand=True)  #pack the treeview into the list window

    def collect_worker_gui(self):
        #create a new window to collect worker info
        new_window = tk.Toplevel(self.root) #open a new window for adding a worker
        new_window.title("Add Worker")  #set the title

        #define labels for input fields
        labels = ["First Name:", "Last Name:", "Position:", "Home Address:", "Birthday (DD.MM.YYYY):", "Phone Number:",
                  "Email:"]
        entries = []  #list containing the entry fields

        #create entry fields with labels
        for label in labels:
            frame = tk.Frame(new_window)  #create a frame for each input field
            frame.pack(fill="x", pady=5)  #pack the frame into the window
            tk.Label(frame, text=label).pack(side="left", padx=5)  # label for the input field
            entry = tk.Entry(frame)  #entry field for user input
            entry.pack(side="right", fill="x", expand=True, padx=5)  #pack the entry field
            entries.append(entry)  #add the entry field to the list

        def submit():
            #get all the data entered by the user
            first_name, last_name, position, home_address, birthday, phone_number, e_mail = [e.get() for e in entries]

            #validate the data using functions from worker_utils.py
            error_message = (
                    first_name_check(first_name) or
                    last_name_check(last_name) or
                    position_check(position) or
                    birthday_check(birthday) or
                    phone_number_check(phone_number) or
                    email_check(e_mail)
            )

            #if validation fails, show an error message
            if error_message:
                messagebox.showerror("Input Error", error_message)
            else:
                #if everything is fine, add the worker info to the list
                new_worker = (f"{first_name} {last_name}", position, home_address, birthday, phone_number, e_mail)
                worker_infos.append(new_worker)
                try:
                    #write the new worker info directly to txt1.txt
                    with open('txt1.txt', 'a') as file:
                        file.write(', '.join(new_worker) + '\n')
                    self.load_worker_infos()  #reload worker_infos to include the new worker
                    messagebox.showinfo("Success", "Worker information added successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Error saving worker data: {str(e)}")
                new_window.destroy()  #close the window after adding the worker

        #button to submit the form
        submit_button = tk.Button(new_window, text="Submit", command=submit)
        submit_button.pack(pady=10)

#this function starts the GUI
def run_gui():
    root = tk.Tk()  #create the root window
    app = WorkerManagerApp(root)  #create an instance of the WorkerManagerApp
    root.geometry("400x400")  #set the size of the window
    root.mainloop()  #start the Tkinter event loop
