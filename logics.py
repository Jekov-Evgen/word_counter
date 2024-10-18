def count(file_name):
    result = ""
    with open(file_name, "r", encoding="UTF-8") as fl:
        result = fl.read()
        
    return len(result.split(' '))