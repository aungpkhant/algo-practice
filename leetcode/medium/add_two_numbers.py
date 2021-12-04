# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = result_tail = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            remainder = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10

            result_tail.next = ListNode(remainder)
            result_tail = result_tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # return the Reference to the next node which is the actual start of the linked list
        return result.next


# if __name__ == "__main__":
# solution = Solution()
# print(solution.addTwoNumbers(l1, l2))
