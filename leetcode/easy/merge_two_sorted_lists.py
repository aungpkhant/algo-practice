# Make a new linked list
# Check the first two nodes
# Take the min of the two
# Iterate to next node for the list to be merged
# Add node to the linked list (set next property)
# Repeat while nodes exist

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        array = []
        curNode = self
        while curNode:
            array.append(str(curNode.val))
            curNode = curNode.next
        return ", ".join(array)


class Solution:
    def mergeTwoLists(self, list1, list2):
        result_tail = result_head = ListNode(0)

        while list1 or list2:
            v1 = list1.val if list1 else float("inf")
            v2 = list2.val if list2 else float("inf")

            if v1 < v2:
                # If we use val from v1
                result_tail.next = list1
                list1 = list1.next
            else:
                result_tail.next = list2
                list2 = list2.next

            result_tail = result_tail.next

        return result_head.next

    # Version that uses recursion
    def recursiveMergeTwoLists(self, l1, l2):
        # if one of either LinkedList is None
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.recursiveMergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.recursiveMergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    l1_head = l1_tail = ListNode(1)
    l1_tail.next = ListNode(2)
    l1_tail = l1_tail.next
    l1_tail.next = ListNode(4)
    l1_tail = l1_tail.next

    l2_head = l2_tail = ListNode(1)
    l2_tail.next = ListNode(3)
    l2_tail = l2_tail.next
    l2_tail.next = ListNode(4)
    l2_tail = l2_tail.next

    print(l1_head)
    print(l2_head)

    solution = Solution()
    print(solution.recursiveMergeTwoLists(l1_head, l2_head))
