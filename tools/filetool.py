def write_text(text, file_name, path="..\\content\\text\\"):
    with open(path + file_name, "wb", encoding='utf-8') as file_obj:
        file_obj.write(text)
        print('write ' + file_name + ' done')


def read_text(file_name, path=".\\content\\text\\"):
    with open(path + file_name, "rb", encoding='utf-8') as io_wrapper:
        print("read " + file_name + " done")
        return io_wrapper
