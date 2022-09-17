NAMES_LIST_PATHNAME = "Day24_MailMerger/Input/Names/invited_names.txt"
TEMPLATE_PATHNAME = "Day24_MailMerger/Input/Letters/starting_letter.txt"
OUTPUT_PATH = "Day24_MailMerger/Output/ReadyToSend/"
PLACEHOLDER = "[name]"


def get_names_list(file_pathname):
    with open(file_pathname, mode='r') as file:
       names_list = file.read().split('\n')
    return names_list


def get_template_text(template_pathname):
    with open(template_pathname, mode='r') as file:
        template_text = file.read()
    return template_text


def create_personalized_letter(name, template_text, ouput_filepath):
    stripped_name = name.strip()
    file_pathname = ouput_filepath + "letter_for_" + stripped_name + ".txt"
    with open(file_pathname, mode='w') as file:
        personalized_text = template_text.replace(PLACEHOLDER, stripped_name)
        file.write(personalized_text)


if __name__ == "__main__":
    names_list = get_names_list(NAMES_LIST_PATHNAME)
    letter_text = get_template_text(TEMPLATE_PATHNAME)

    for name in names_list:
        create_personalized_letter(name, letter_text, OUTPUT_PATH)

