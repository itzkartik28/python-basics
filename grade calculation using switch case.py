grade=input("enter a grade(a/b/c/d):")

match grade:

    case "a":
        print("excellent")

    case "b":
        print("very good")

    case "c":
        print("good")

    case "d":
        print("pass")

    case _:
        print("invalid grade!!")