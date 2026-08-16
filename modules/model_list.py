from ollama import list as ollama_list

def model_lister():
    models_list, models_list_edited= [], []
    response = ollama_list()
    for item in response.models:
        name = str(item.model)
        if '/' not in name:
            models_list += [name]
            name_split = name.split(':', 1)[0]
            models_list_edited += [name_split.lower()]
    return sorted(models_list), sorted(models_list_edited)

if __name__ == "__main__":
    models, models_edited = model_lister()
    print(sorted(models))
