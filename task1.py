class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next
      
  def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
    
    
  def insertion_sort(self):
    sorted_list = None  # Починаємо з порожнього відсортованого списку
    current = self.head
    
    while current:
        next_node = current.next  # Запам'ятовуємо наступний вузол
        sorted_list = self.sorted_insert(sorted_list, current)  # Вставляємо поточний вузол у відсортований список
        current = next_node  # Переходимо до наступного вузла
        
    self.head = sorted_list  # Встановлюємо голову на відсортований список

  def sorted_insert(self, sorted_list, new_node):
    # Вставляє новий вузол у відсортований список
    if sorted_list is None or new_node.data < sorted_list.data:
        new_node.next = sorted_list
        return new_node
    
    current = sorted_list
    while current.next and current.next.data < new_node.data:
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return sorted_list

  def merge_two_sorted_lists(self, other_list):
    # Початок об'єднаного списку з "заглушкою" для зручності
    dummy = Node(0)
    tail = dummy
    
    left = self.head
    right = other_list.head
    
    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next  # Переміщуємо хвіст до наступного вузла
    
    # Додаємо залишки з одного зі списків, якщо є
    tail.next = left if left else right
    
    # Оновлюємо голову поточного списку на початок об'єднаного списку
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.print_list()

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(8)
list2.insert_at_end(6)
list2.print_list()

# Реверсування першого списку
print("Реверсований список 1:")
list1.reverse()
list1.print_list()

# Сортування другого списку
print("\nВідсортований список 2:")
list2.insertion_sort()
list2.print_list()

# Об'єднання двох відсортованих списків
list1.reverse()
merged_list = list1.merge_two_sorted_lists(list2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()