from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def test_middleNode():
    # Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Call the function and check the output
    solution = Solution()
    middle_node = solution.middleNode(head)
    assert middle_node is not None
    assert middle_node.val == 3
    assert middle_node.next is not None
    assert middle_node.next.val == 4
    assert middle_node.next.next.val == 5
    assert middle_node.next.next.next is None


def test_middleNode_2():
    # Create the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    # Call the function and check the output
    solution = Solution()
    middle_node = solution.middleNode(head)
    assert middle_node is not None
    assert middle_node.val == 4
    assert middle_node.next is not None
    assert middle_node.next.val == 5
    assert middle_node.next.next.val == 6
    assert middle_node.next.next.next is None


def test_middleNode_3():
    # Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Call the function and check the output
    solution = Solution()
    middle_node = solution.middleNode(head)
    assert middle_node is not None
    assert middle_node.val == 3
    assert middle_node.next is not None
    assert middle_node.next.val == 4
    assert middle_node.next.next.val == 5
    assert middle_node.next.next.next is None

    # Modify the linked list to remove the first two nodes
    head = head.next.next

    # Call the function again and check the output
    middle_node = solution.middleNode(head)
    assert middle_node is not None
    assert middle_node.val == 4
    assert middle_node.next is not None
    assert middle_node.next.val == 5
    assert middle_node.next.next is None
