import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Manager")

        # Adding menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="View Contacts", command=self.view_contacts)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Adding New Contact Frame
        self.add_frame = tk.LabelFrame(self.root, text="Add New Contact", padx=10, pady=10)
        self.add_frame.pack(padx=10, pady=10, fill="x")

        # Creating entry fields for details of contact
        self.name_label = tk.Label(self.add_frame, text="Name")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.add_frame)
        self.name_entry.grid(row=0, column=1, pady=2, padx=5, sticky="w")

        self.phone_label = tk.Label(self.add_frame, text="Phone Number")
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(self.add_frame)
        self.phone_entry.grid(row=1, column=1, pady=2, padx=5, sticky="w")

        # Button to add new contact
        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, columnspan=2, pady=10)

        # Frame for viewing the contact list
        self.view_frame = tk.Frame(self.root)
        self.view_frame.pack(pady=10)

        # Creating a listbox to display contacts
        self.contacts_listbox = tk.Listbox(self.view_frame, width=50)
        self.contacts_listbox.pack()

        # On double click the element/contact should be selected
        self.contacts_listbox.bind("<Double-1>", self.select_contact)

        # Buttons for update and delete
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Button to update and delete a selected contact, which triggers the update_contact method when clicked
        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=0, padx=5)
        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Search Contact Frame
        self.search_frame = tk.LabelFrame(self.root, text="Search Contact", padx=10, pady=10)
        self.search_frame.pack(padx=10, pady=10, fill="x")

        # Entry fields for searching the contact
        self.search_label = tk.Label(self.search_frame, text="Search by Name or Phone Number")
        self.search_label.grid(row=0, column=0, sticky="e")
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1, pady=2, padx=5, sticky="w")

        # Button to execute search
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=1, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append({"name": name, "phone": phone})
            self.contacts_listbox.insert(tk.END, f"{name} - {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and Phone Number are required!")

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def select_contact(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact['phone'])

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            if name and phone:
                self.contacts[index] = {"name": name, "phone": phone}
                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showwarning("Warning", "Name and Phone Number are required!")
        else:
            messagebox.showwarning("Warning", "No contact selected!")

    def search_contact(self):
        search_query = self.search_entry.get().lower()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_query in contact['name'].lower() or search_query in contact['phone']:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            del self.contacts[index]
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No contact selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
