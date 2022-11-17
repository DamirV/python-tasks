from collections import deque


def is_correct_brackets_v1(brackets):
    stack = deque()

    for i in brackets:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif i == ")" or i == "}" or i == "]":
            if len(stack) == 0 or i != stack[-1]:
                return False
            stack.pop()

    return len(stack) == 0


def is_correct_brackets_v2(brackets):
    stack = deque()
    brackets_dict = {"[": "]", "{": "}", "(": ")"}

    for i in brackets:
        if i == "(" or i == "[" or i == "{":
            stack.append(brackets_dict[i])
        elif i == ")" or i == "]" or i == "}":
            if len(stack) == 0 or i != stack[-1]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    brackets_right1 = "abc[]{[({{}})[]]}"
    brackets_right2 = ""
    brackets_right3 = "abc"
    brackets_right4 = "[(){}]abc"
    brackets_right5 = "abc"
    brackets_right6 = '(":-[];)'
    brackets_right7 = 'print(f"Expect True: {is_correct_brackets_v2(brackets_right7)}")'
    brackets_wrong1 = "{[(]}"
    brackets_wrong2 = "{[)]}"
    brackets_wrong3 = "abc}"
    brackets_wrong4 = "(abc"

    print(f"Expect True: {is_correct_brackets_v2(brackets_right1)}")
    print(f"Expect True: {is_correct_brackets_v2(brackets_right2)}")
    print(f"Expect True: {is_correct_brackets_v2(brackets_right3)}")
    print(f"Expect True: {is_correct_brackets_v2(brackets_right4)}")
    print(f"Expect True: {is_correct_brackets_v2(brackets_right5)}")
    print(f"Expect True: {is_correct_brackets_v2(brackets_right6)}")
    print(f"Expect True: {is_correct_brackets_v2(brackets_right7)}")
    print(f"Expect False: {is_correct_brackets_v2(brackets_wrong1)}")
    print(f"Expect False: {is_correct_brackets_v2(brackets_wrong2)}")
    print(f"Expect False: {is_correct_brackets_v2(brackets_wrong3)}")
    print(f"Expect False: {is_correct_brackets_v2(brackets_wrong4)}")
