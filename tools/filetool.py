from tools.exception import TextCannotWrite, TextCannotRead


def write_text(text, file_name, path="..\\content\\text\\"):
    try:
        with open(path + file_name, "w",encoding='utf-8') as file_obj:
            file_obj.write(text)
            print('write ' + file_name + ' done')
    except:
        raise TextCannotWrite

def read_text(file_name, path=".\\content\\text\\"):
    try:
        with open(path + file_name, "rb", encoding='utf-8') as io_wrapper:
            print("read " + file_name + " done")
            return io_wrapper
    except:
        raise TextCannotRead