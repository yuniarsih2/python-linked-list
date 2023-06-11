#Membuat program menggunakan single linked list untuk menambahkan tugas baru, menghapus tugas dan mencetak dftar tugas berdasarkan prioritas
class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Node(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            if priority < current.priority:
                new_task.next = current
                self.head = new_task
            else:
                while current.next and priority >= current.next.priority:
                    current = current.next
                new_task.next = current.next
                current.next = new_task

    def remove_task(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.description != description:
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_tasks(self):
        if self.head is None:
            print("Tidak ada tugas dalam daftar.")
            return

        current = self.head
        print("Daftar Tugas:")
        while current:
            print(f"Deskripsi: {current.description}, Prioritas: {current.priority}")
            current = current.next

# Contoh penggunaan program
task_list = TaskList()

# Menambahkan tugas baru
task_list.add_task("Mengerjakan laporan", 3)
task_list.add_task("Mengirim email", 2)
task_list.add_task("Berkumpul dengan tim", 1)

# Mencetak daftar tugas
task_list.print_tasks()
# Output:
# Daftar Tugas:
# Deskripsi: Berkumpul dengan tim, Prioritas: 1
# Deskripsi: Mengirim email, Prioritas: 2
# Deskripsi: Mengerjakan laporan, Prioritas: 3

# Menghapus tugas
task_list.remove_task("Mengirim email")

# Mencetak daftar tugas setelah menghapus tugas
task_list.print_tasks()
# Output:
# Daftar Tugas:
# Deskripsi: Berkumpul dengan tim, Prioritas: 1
# Deskripsi: Mengerjakan laporan, Prioritas: 3
