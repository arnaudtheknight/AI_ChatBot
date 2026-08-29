# Imports:
from ollama import list as ollama_list

# Model lister:
def list_models():
    list_official, list_edited= [], []
    response = ollama_list()
    for item in response.models:
        name = str(item.model) # call str() to use split() later
        if "hf.co/" not in name:
            list_official += [name] # ModelName:version
            name_split = name.split(':', 1)[0]
            list_edited += [name.lower()]
            list_edited += [name_split.lower()] # modelname
    return sorted(list_official), sorted(list_edited)

if __name__ == "__main__":
    official, edited = list_models()
    print(official)
    print(edited)
