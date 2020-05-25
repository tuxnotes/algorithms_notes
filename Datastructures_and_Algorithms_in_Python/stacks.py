class Empty(Exception):
    """Error attempting to access an element from an emplty container"""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empyty stack"""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of element in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self):
        """Add element e to the top of the stack"""
        self._data.append(e)  # new item stored at end of list

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Some time top operation is also called peek.
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]



def reverse_file(filename):
    """Overwrite given file with its contents line-by-line erversed"""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))  # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents if LIFO order
    output = open(filename, 'w')   # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()


def is_matched(expr):
    """Return True if all delimiter are properly match; False otherwise"""
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()   # were all symbols matched


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise"""
    S = ArrayStack()
    j = raw.find('<')  # find the first '<' character(if any)
    while j != -1:
        k = raw.find('>', j+1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        tag = raw[j+1:k]  # strip away < >
        if not tag.startswith('/'):  # this is opening tag
            S.push(tag)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k+1)  # find next '<' character (if any)
    return S.is_empty()  # were all opening tags matched?


# find(...) method of buildins.str instance
# S.find(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end]. start and 
# ed are interpreted as in slice notation.
# Return -1 on failure