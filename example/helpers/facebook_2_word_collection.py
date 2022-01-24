import os
import json

from tqdm import tqdm
from pathlib import Path


def _get_facebook_paths():
    for file_name in os.listdir("."):
        if "facebook" not in file_name or ".zip" in file_name:
            continue
        unformatted_facebook_paths = [x for x in os.walk(f"./{file_name}/messages/inbox")]
        facebook_parent_folder = unformatted_facebook_paths.pop(0)

        formatted_facebook_paths = [{
            "folder_name": facebook_parent_folder[1][unformatted_facebook_paths.index(path_info)],
            "message_paths": [os.path.join(path_info[0], message_path) for message_path in path_info[2]],
            "path": path_info[0],
        } for path_info in unformatted_facebook_paths]
        return formatted_facebook_paths


def _parse_message_json(message_json):
    message_list = message_json["messages"]
    message_content_list = []
    for message in message_list:
        if "content" not in message:
            continue
        message_content = message["content"]
        message_content_list.append(message_content)
    return message_content_list


def facebook_2_word_collection(facebook_filename=None):
    for formatted_paths in _get_facebook_paths():
        if facebook_filename and facebook_filename != formatted_paths["folder_name"]:
            continue
        messages = []
        print(f"Getting JSON of {formatted_paths['message_paths']}...")
        for message_paths in formatted_paths["message_paths"]:
            with open(message_paths, "r") as json_file:
                messages_json = json.load(json_file)
                parsed_json = _parse_message_json(messages_json)
                messages += parsed_json

        print(f"Printing messages at {'./temp/word_collection/' + formatted_paths['folder_name'] + '.txt'}...")
        Path("./temp/word_collection").mkdir(parents=True, exist_ok=True)
        with tqdm(total=len(messages)) as pbar:
            with open(f"temp/word_collection/{formatted_paths['folder_name']}.txt", "w", encoding="utf-8") as new_file:
                for message in messages:
                    new_file.write(message + "\n")
                    pbar.update(len(message))
