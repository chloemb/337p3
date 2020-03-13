from retriever import retrieve_dict

recipe = retrieve_dict()

print('Now cooking:', recipe['Name'])
print('Please type a request.')
print('To ask a question, use the following format: \'How do I <technique>?\' or \'What is a <tool>?\'')
while True:
    request_string = input()

    later_change_with_how_present_check = False

    later_change_with_what_present_check = False
    butts = False

    # add code here

    if "How do I" in request_string:
        request_string_how = request_string.split("I", 1)[1]
        url_string = "https://www.youtube.com/results?search_query=how+to"+request_string_how.replace(" ", "+").replace('?', '')
        print("No worries. I found a reference for you: " + url_string)
        butts = True

    if "What is a" in request_string:
        request_string_what = request_string.split(" a ", 1)[1]
        request_string_what.replace('?', '')
        url_string = "https://en.wikipedia.org/wiki/" + request_string_what.replace(" ", "_").replace('?', '')
        print("No worries. I found a reference for you: " + url_string)
        butts = True

    if butts:
        print("Any further requests?")
    else:
        print("Invalid response, try again")

