"""링크드 리스트를 클래스로 만들었으니까 링크드 리스트를 문자열로 표현해주는
__str__ 메소드를 정의해봅시다. __str__메소드가 기억 안나시는 분들은
그냥 링크드 리스트를 출력할 때 자동으로 링크드 리스트의 내용을 사람들이 이해할 수 있는
문자열로 리턴해주는 메소드로 이해하시면 됩니다."""

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self,data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        #링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자
        #마지막 노드
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  #가장 마지막 노드 뒤에 새로운 노드를 추가
            self.tail = new_node  #마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        #링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        #링크드 리스트 끝까지 돈다.
        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str

#새로운 링크드 리스트 생성
linked_list = LinkedList()

#링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)