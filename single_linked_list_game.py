# membuat program game menggunakan single linked list untuk menambahkan item ke dalam tas, menghapus item, dan mencetak daftar item berdasarkan tingkat kepentingan
class Node:
    def __init__(self, item_name, importance_level):
        self.item_name = item_name
        self.importance_level = importance_level
        self.next = None


class PlayerInventory:
    def __init__(self):
        self.head = None

    def add_item(self, item_name, importance_level):
        new_item = Node(item_name, importance_level)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            if importance_level < current.importance_level:
                new_item.next = current
                self.head = new_item
            else:
                while (
                    current.next and importance_level >= current.next.importance_level
                ):
                    current = current.next
                new_item.next = current.next
                current.next = new_item

    def remove_item(self, item_name):
        if self.head is None:
            return

        if self.head.item_name == item_name:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.item_name != item_name:
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_inventory(self):
        if self.head is None:
            print("Tas pemain kosong.")
            return

        current = self.head
        print("Isi Tas Pemain:")
        while current:
            print(
                f"Nama Item: {current.item_name}, Tingkat Kepentingan: {current.importance_level}"
            )
            current = current.next


# Contoh penggunaan program
inventory = PlayerInventory()


class Node:
    def __init__(self, item_name, importance_level):
        self.item_name = item_name
        self.importance_level = importance_level
        self.next = None


class PlayerInventory:
    def __init__(self):
        self.head = None

    def add_item(self, item_name, importance_level):
        new_item = Node(item_name, importance_level)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            if importance_level < current.importance_level:
                new_item.next = current
                self.head = new_item
            else:
                while (
                    current.next and importance_level >= current.next.importance_level
                ):
                    current = current.next
                new_item.next = current.next
                current.next = new_item

    def remove_item(self, item_name):
        if self.head is None:
            return

        if self.head.item_name == item_name:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.item_name != item_name:
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_inventory(self):
        if self.head is None:
            print("Tas pemain kosong.")
            return

        current = self.head
        print("Isi Tas Pemain:")
        while current:
            print(
                f"Nama Item: {current.item_name}, Tingkat Kepentingan: {current.importance_level}"
            )
            current = current.next


# Contoh penggunaan program
inventory = PlayerInventory()

# Menambahkan item ke dalam tas pemain
inventory.add_item("Pedang", 3)
inventory.add_item("Potion", 2)
inventory.add_item("Perisai", 1)
inventory.add_item("Buku Sihir", 2)

# Mencetak daftar item dalam tas pemain
inventory.print_inventory()
# Output:Isi Tas Pemain:
# Nama Item: Perisai, Tingkat Kepentingan: 1
# Nama Item: Potion, Tingkat Kepentingan: 2
# Nama Item: Buku Sihir, Tingkat Kepentingan: 2
# Nama Item: Pedang, Tingkat Kepentingan: 3

# Menghapus item dari tas pemain
inventory.remove_item("Potion")

# Mencetak daftar item setelah menghapus item
inventory.print_inventory()
# Output: Isi Tas Pemain:
# Nama Item: Perisai, Tingkat Kepentingan: 1
# Nama Item: Buku Sihir, Tingkat Kepentingan: 2
# Nama Item: Pedang, Tingkat Kepentingan: 3
# Menambahkan item ke dalam tas pemain
inventory.add_item("Pedang", 3)
inventory.add_item("Potion", 2)
inventory.add_item("Perisai", 1)
inventory.add_item("Buku Sihir", 2)

# Mencetak daftar item dalam tas pemain
inventory.print_inventory()
# Output: Isi Tas Pemain:
# Nama Item: Perisai, Tingkat Kepentingan: 1
# Nama Item: Potion, Tingkat Kepentingan: 2
# Nama Item: Buku Sihir, Tingkat Kepentingan: 2
# Nama Item: Pedang, Tingkat Kepentingan: 3

# Menghapus item dari tas pemain
inventory.remove_item("Potion")

# Mencetak daftar item setelah menghapus item
inventory.print_inventory()
# Output: Isi Tas Pemain:
# Nama Item: Perisai, Tingkat Kepentingan: 1
# Nama Item: Buku Sihir, Tingkat Kepentingan: 2
# Nama Item: Pedang, Tingkat Kepentingan: 3
