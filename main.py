from retriever import retrieve_dict
import sys

recipe = retrieve_dict()

next_words = ['next', 'got it', 'okay', 'cool', 'then', 'after']
previous_words = ['previous', 'before']
repeat_words = ['again', 'repeat', 'sorry', 'current']
ing_req_words = ['ingredients', 'everything']

first_words = ['first', '1', 'start', 'begin']
final_words = ['final', 'last']

exit_words = ['stop', 'quit', 'exit']

print('Now cooking:', recipe['Name'])
print('Please type a request.')
current_step = 0

print('To ask a question, use the following format: \'How do I <technique>?\' or \'What is a <tool>?\'')


def main_fun():
    request_string = input()
    answer_string = request_loop(request_string)
    print(answer_string)
    if answer_string == '\nExiting...\n':
        sys.exit()
    main_fun()


def request_loop(request_string):
    global current_step
    request_string = request_string.lower()

    later_change_with_how_present_check = False

    later_change_with_what_present_check = False

    # add code here

    if any(word in request_string for word in exit_words):
        return '\n' + 'Exiting...' + '\n'

    if any(word in request_string for word in next_words):
        current_step += 1
        if not current_step > len(recipe['Procedure']) - 1:
            return '\n' + 'The next step is:\n' + str(current_step) + ': ' + recipe['Procedure'][current_step] + '\n'
        else:
            return '\n' + 'End of recipe reached. Continue entering commands or request to exit.' + '\n'
    elif any(word in request_string for word in previous_words):
        current_step -= 1
        return '\n' + 'The previous step is:\n' + str(current_step) + ': ' + recipe['Procedure'][current_step] + '\n'
    elif any(word in request_string for word in repeat_words):
        return '\nThe current step is:\n' + str(current_step) + ': ' + recipe['Procedure'][current_step] + '\n'
    elif any(word in request_string for word in ing_req_words):
        print_count = 0
        final_string = 'Here are all the ingredients:\n'
        for ing in recipe['Ingredients']:
            print_count += 1
            final_string += ing + '\n'
        return '\n' + final_string
    elif any(word in request_string for word in first_words):
        current_step = 0
        return '\n' + 'The first step is:\n' + str(current_step) + ': ' + recipe['Procedure'][0] + '\n'
    elif 'step' in request_string:
        if 'all' in request_string:
            print_count = 0
            final_string = 'Here are all the steps:\n'
            for step in recipe['Procedure']:
                print_count += 1
                final_string += str(print_count) + ": " + step + '\n'
            return '\n' + final_string
        elif any(word in request_string for word in final_words):
            current_step = len(recipe['Procedure']) - 1
            return '\n' + 'The final step is:\n' + str(current_step) + ': ' + recipe['Procedure'][-1] + '\n'

    if "how do i" in request_string:
        request_string_how = request_string.split("i", 1)[1]
        url_string = "https://www.youtube.com/results?search_query=how+to"+request_string_how.replace(" ", "+").replace('?', '')
        return '\n' + "No worries. I found a reference for you: " + url_string + '\n'

    if "what is a" in request_string:
        request_string_what = request_string.split(" a ", 1)[1]
        request_string_what.replace('?', '')
        url_string = "https://en.wikipedia.org/wiki/" + request_string_what.replace(" ", "_").replace('?', '')
        return '\n' + "No worries. I found a reference for you: " + url_string + '\n'

    return '\n' + "Sorry, I don't understand that. Please try a different request or rephrase this one?"


main_fun()
