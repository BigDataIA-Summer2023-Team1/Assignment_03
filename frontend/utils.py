import json


def fetch_files(directory):
    # file_list = []
    # for root, dirs, files in os.walk(directory):
    #     for file in files:
    #         file_path = os.path.join(root, file)
    #         file_list.append(file_path)

    with open("./files.json") as f:
        file_list = json.load(f)
    return file_list
