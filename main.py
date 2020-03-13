from retriever import retrieve_dict

recipe = retrieve_dict()

print('Now cooking:', recipe['Name'])
print('Please type a request.')
request_string = input()

# add code here