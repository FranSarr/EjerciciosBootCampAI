from openai import OpenAI

client = OpenAI()

model = "gpt-3.5-turbo"

def handle_option(option, dish=None, ingredients=None, recipe=None):
    if option == 1:
        return f"Suggest dishes based on ingredients: {ingredients}\n"
    elif option == 2:
        return f"Give recipes to dish: {dish}\n"
    elif option == 3:
        return f"Criticize the recipe: {recipe}\n"
    else:
        return "Invalid option selected.\n"

def prompt_user():
    print("Select an option (1-3):")
    print("1. Suggest dishes based on ingredients")
    print("2. Give recipes to dishes")
    print("3. Criticize recipes")
    
    while True:
        option = input()
        if option.isdigit():
            option = int(option)
            if option in [1, 2, 3]:
                if option == 1:
                    ingredients = input("Enter ingredients:\n")
                    return option, ingredients
                elif option == 2:
                    dish = input("Type the name of the dish you want a recipe for:\n")
                    if not dish:
                        print("Please provide a dish name.")
                        continue
                    return option, dish
                elif option == 3:
                    recipe = input("Enter the recipe to criticize:\n")
                    return option, recipe
            else:
                print("Invalid option. Please select a number between 1 and 3.")
        else:
            print("Invalid input. Please enter a number.")

while True:
    messages = [
        {
            "role": "system",
            "content": "You are an amateur spanish cook that loves traditional Mediterranean recipes",
        },
        {
            "role": "system",
            "content": "Your client is going to ask for three different possible inputs: \n1. Suggest dishes based on ingredients \n2. Give recipes to dishes \n3. Criticize recipes",
        }
    ]

    option, data = prompt_user()
    messages.append(
        {
            "role": "user",
            "content": data
        }
    )

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

    choice = input("\nDo you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        break