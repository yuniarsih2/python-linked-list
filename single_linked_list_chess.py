# membuat program catur menggunakan single linked list untuk mendaftarkan peserta, menghapus peserta yang telah kalah, dan mencetak daftar peserta berdasarkan peringkat
class Node:
    def __init__(self, player_name, ranking):
        self.player_name = player_name
        self.ranking = ranking
        self.next = None


class ChessTournament:
    def __init__(self):
        self.head = None

    def register_player(self, player_name, ranking):
        new_player = Node(player_name, ranking)
        if self.head is None:
            self.head = new_player
        else:
            current = self.head
            if ranking < current.ranking:
                new_player.next = current
                self.head = new_player
            else:
                while current.next and ranking >= current.next.ranking:
                    current = current.next
                new_player.next = current.next
                current.next = new_player

    def eliminate_player(self, player_name):
        if self.head is None:
            return

        if self.head.player_name == player_name:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.player_name != player_name:
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_players(self):
        if self.head is None:
            print("Tidak ada peserta terdaftar.")
            return

        current = self.head
        print("Daftar Peserta Turnamen:")
        while current:
            print(f"Nama: {current.player_name}, Peringkat: {current.ranking}")
            current = current.next


# Contoh penggunaan program
tournament = ChessTournament()

# Mendaftarkan peserta turnamen
tournament.register_player("Andi", 1200)
tournament.register_player("Budi", 1500)
tournament.register_player("Cindy", 1100)
tournament.register_player("Dodi", 1300)

# Mencetak daftar peserta turnamen
tournament.print_players()
# Output:
# Daftar Peserta Turnamen:
# Nama: Cindy, Peringkat: 1100
# Nama: Andi, Peringkat: 1200
# Nama: Dodi, Peringkat: 1300
# Nama: Budi, Peringkat: 1500

# Menghapus peserta yang telah kalah
tournament.eliminate_player("Andi")

# Mencetak daftar peserta setelah menghapus peserta
tournament.print_players()
# Output:
# Daftar Peserta Turnamen:
# Nama: Cindy, Peringkat: 1100
# Nama: Dodi, Peringkat: 1300
# Nama: Budi, Peringkat: 1500
