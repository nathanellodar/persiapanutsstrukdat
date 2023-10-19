class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None

class StackADT:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self,data):
        baru = Node(data)
        if self.tail == None:
            self.head = baru
            self.tail = baru
            self.tail.next = None
        else:
            self.tail.next = baru
            self.tail = baru
        self.size += 1

    def top(self):
        return f" top dalam stack ini adalah {self.head.data}"

    def pop(self):
        if self.size > 0:
            delete_node = self.head
            self.head = self.head.next
            delete_node.next = None
            self.size -= 1
            data = delete_node.data
            del delete_node
            return data
        else:
            print(" stack kosong ")

    def deleteByData(self, data):
        if self.size > 0:
            helper = self.head
            node_before_helper = 0
            while helper != None:
                if helper.data == data:
                    node_before_helper.next = helper.next
                    helper.next = None
                    print(f"data  berhail dihapus", helper.data)
                    del helper
                    self.size -= 1
                    break
                else:
                    node_before_helper =  helper
                    helper = helper.next
        else:
            print(" stack kosong ")

    def __str__(self):
        if self.size > 0:
            helper = self.head
            String = ""
            while helper != None:
                String += f' {helper.data}'
                helper = helper.next
            return String
        else:
            return (" stack kosong ")


if __name__ == "__main__":
    var_list = []
    susunan_asli = []
    stack = StackADT()
    for i in range(10):
        data = input('Masukan angka: ')
        if data not in var_list:
            var_list.append(data)
            stack.push(data)
            susunan_asli.append(data)
            print(f'isi: {stack.__str__()}')
        else:
            posisi = var_list.index(data)
            var_list.insert(posisi, data)
            for hapus in range(len(susunan_asli)):
                stack.pop()
            stack.tail = None
            for isi in var_list:
                stack.push(isi)
            print(f'isi: {stack.__str__()}')
