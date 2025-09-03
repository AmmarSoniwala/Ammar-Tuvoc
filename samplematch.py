a = "bold"
match a:
    case "italic":
        print("This is italic")
    case "underline":
        print("This is Underline")
    case "bold":
        print("This is Bold")
    case _:
        print("No match")
