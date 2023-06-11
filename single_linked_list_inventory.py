# membuat program menggunakan single linked list untuk menambahkan produk baru, menghapus produk, dan mencetak daftar produk beserta jumlah stoknya
class Node:
    def __init__(self, product_name, product_code, stock):
        self.product_name = product_name
        self.product_code = product_code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, product_name, product_code, stock):
        new_product = Node(product_name, product_code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            if product_code < current.product_code:
                new_product.next = current
                self.head = new_product
            else:
                while current.next and product_code >= current.next.product_code:
                    current = current.next
                new_product.next = current.next
                current.next = new_product

    def remove_product(self, product_code):
        if self.head is None:
            return

        if self.head.product_code == product_code:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.product_code != product_code:
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_inventory(self):
        if self.head is None:
            print("Inventaris kosong.")
            return

        current = self.head
        print("Daftar Inventaris Produk:")
        while current:
            print(
                f"Nama Produk: {current.product_name}, Kode Produk: {current.product_code}, Stok: {current.stock}"
            )
            current = current.next


# Contoh penggunaan program
inventory = InventoryManagement()

# Menambahkan produk ke dalam inventaris
inventory.add_product("Laptop", 12345, 10)
inventory.add_product("Smartphone", 56789, 20)
inventory.add_product("Printer", 24680, 5)
inventory.add_product("Tablet", 13579, 15)

# Mencetak daftar inventaris produk
inventory.print_inventory()
# Output:
# Daftar Inventaris Produk:
# Nama Produk: Printer, Kode Produk: 24680, Stok: 5
# Nama Produk: Tablet, Kode Produk: 13579, Stok: 15
# Nama Produk: Laptop, Kode Produk: 12345, Stok: 10
# Nama Produk: Smartphone, Kode Produk: 56789, Stok: 20

# Menghapus produk dari inventaris
inventory.remove_product(12345)

# Mencetak daftar inventaris produk setelah menghapus produk
inventory.print_inventory()
# Output:
# Daftar Inventaris Produk:
# Nama Produk: Printer, Kode Produk: 24680, Stok: 5
# Nama Produk: Tablet, Kode Produk: 13579, Stok: 15
# Nama Produk: Smartphone, Kode Produk: 56789, Stok: 20
