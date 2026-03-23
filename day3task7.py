# Python program to demonstrate list operations

def main():
    try:
        # Step 1: Create an empty list
        my_list = []

        # Step 2: Add 3 elements using append()
        print("Enter 3 elements to append to the list:")
        for i in range(3):
            element = input(f"Element {i+1}: ")
            my_list.append(element)

        print("\nList after appending 3 elements:", my_list)

        # Step 3: Insert element at a specific index
        element_to_insert = input("\nEnter element to insert: ")
        index = input("Enter index to insert at (0-based): ")

        if not index.isdigit() or int(index) < 0 or int(index) > len(my_list):
            print("Invalid index. Skipping insertion.")
        else:
            my_list.insert(int(index), element_to_insert)
            print("List after insertion:", my_list)

        # Step 4: Remove element using remove()
        element_to_remove = input("\nEnter element to remove: ")
        if element_to_remove in my_list:
            my_list.remove(element_to_remove)
            print("List after removal:", my_list)
        else:
            print("Element not found. Skipping removal.")

        # Step 5: Reverse list without using .reverse()
        reversed_list = my_list[::-1]
        print("\nList reversed (without .reverse()):", reversed_list)

        # Step 6: Sort list without using .sort()
        # Using Bubble Sort for demonstration
        sorted_list = my_list[:]
        n = len(sorted_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if str(sorted_list[j]) > str(sorted_list[j + 1]):
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

        print("List sorted (without .sort()):", sorted_list)

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
