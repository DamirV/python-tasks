from collections import deque


def is_correct_brackets(brackets):
    stack = deque()
    for i in brackets:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif len(stack) == 0 or i != stack[-1]:
            return False
        else:
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    brackets_right1 = "[]{[({{}})[]]}"
    brackets_right2 = ""
    brackets_wrong1 = "{[(]}"
    brackets_wrong2 = "{[)]}"
    brackets_wrong3 = "}"
    brackets_wrong4 = "("

    print(f"Expect True: {is_correct_brackets(brackets_right1)}")
    print(f"Expect True: {is_correct_brackets(brackets_right2)}")
    print(f"Expect False: {is_correct_brackets(brackets_wrong1)}")
    print(f"Expect False: {is_correct_brackets(brackets_wrong2)}")
    print(f"Expect False: {is_correct_brackets(brackets_wrong3)}")
    print(f"Expect False: {is_correct_brackets(brackets_wrong4)}")
