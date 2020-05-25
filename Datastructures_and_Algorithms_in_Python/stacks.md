# Stacks

A stack is a **collection of objcts** that are **inserted and removed according to the LIFO** principle.

## Application

- Internet Web browsers store the address of the recently visited sites in a stack. Each time a user visits a new site, that site's address is "pushed" onto the stack of addresses. The browser then allows the user to "pop" back to previously visited sites using the "back" button.

- Text editors usually provide an **"undo"** mechanism that cancels recent editing operations and reverts to former states of a document. This undo operation can be accomplished by keeping text changes in a stack.

- Reversing data using a stack. As a consequence of the LIFO protocol, a stack can be used as a general tool to reverse a data sequence. The idea can be applied in a varity fo settings. For example, we might wish to print lines of a file in reverse order in order to display a data set in decreasing order rather than increasing order.

- Matching parentheses and HTML tags.**An algorithms for mathcing delimiters**. 
    - Assuming the input is a sequence of characters. We perform a left-to-right scan of the original sequence, using a stack S to facilitate the mathcing of grouping symbols
    - Each time we encounter an openning symbol, we push that symbool onto S, and each time we encounter a closing symbol, we pop a symbol from the stack S(assuming S is not empty), and check that these two symbols form a valid pair.
    - If we reach the end of the expression and the stack isempty, then the original expression was properly matched. Otherwise, there must be an opening delimiter on the stack without a matching symbol.