def merge_lists(ll_one, ll_two):
    """Create a zipper like function that will merge two linked lists."""
    if len(ll_one) > len(ll_two):
        current1, current2 = ll_one.head._next, ll_two.head

        while current2 is not None:
            ll_one.insertBefore(current1.val, current2.val)
            current1, current2 = current1._next, current2._next

        return ll_one.head.val

    else:
        current1, current2 = ll_one.head, ll_two.head
        while current1 is not None:
            ll_two.insertBefore(current2.val, current1.val)
            current2, current1 = current2._next, current1._next

        return ll_two.head.val
