
file_path = "data/notes.txt"



def load_notes(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        paragraphs = content.split("\n\n")
        paragraphs = [p.strip() for p in paragraphs]

        return paragraphs

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []


def search_notes(query, paragraphs):
    if not query.strip():
        return []

    results = []

    for paragraph in paragraphs:
        score = paragraph.lower().count(query.lower())
        if score > 0:
            # Add paragraph and score to results
              results.append((paragraph, score))
    ranked_results =sorted(
         results,
         key=lambda item: item[1],
         reverse=True
     )
    return ranked_results



def display_results(results):

    if not results:
        print("No matching information found.")
        return

    print("\n===== SEARCH RESULTS =====")

    for paragraph, score in results:
        print(f"\nRelevance Score: {score}")
        print(paragraph)



def main():

    file_path = "data/notes.txt"

    paragraphs = load_notes(file_path)

    if not paragraphs:
        print("No notes available.")
        return

    print("===== WELCOME TO STUDYLENS =====")
    print("Type 'exit' to close StudyLens.")

    while True:

        query = input("\nWhat do you want to search? ")

        # Exit condition
        if query.lower().strip() == "exit":
            print("Thank you for using StudyLens!")
            break

        # Search and display results
        results = search_notes(query, paragraphs)

        display_results(results)


if __name__ == "__main__":
    main()
