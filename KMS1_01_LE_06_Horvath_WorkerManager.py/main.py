from worker_utils import collect_worker_info, show_worker_list, filter_and_show_worker_list, edit_worker, \
    filter_and_export, worker_infos, export_to_file, show_filtered_workers
from workerGUI import run_gui

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add worker")
        print("2. Show unfiltered worker list")
        print("3. Show filtered worker list")
        print("4. Filter list")
        print("5. Edit worker")
        print("6. Filter by birth month and export")
        print("7. Close program")

        choice = input("Please enter your choice (1/2/3/4/5/6/7): ").strip()

        if choice == '1':
            collect_worker_info()
            export_to_file('txt1.txt')
        elif choice == '2':
            show_worker_list(worker_infos)  #show the unfiltered list
        elif choice == '3':
            show_filtered_workers()  #show the filtered list
        elif choice == '4':
            filter_and_show_worker_list()  #apply filter and display filtered list
        elif choice == '5':
            edit_worker()
        elif choice == '6':
            filter_and_export()  #filter by birth month and export results
        elif choice == '7':
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    run_gui()

