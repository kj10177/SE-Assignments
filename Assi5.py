class FamilyMember:
    def __init__(self, name, family_name, birthdate):
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate
        self.children = []

def add_family_member(parent, name, family_name, birthdate):
    new_member = FamilyMember(name, family_name, birthdate)
    parent.children.append(new_member)
    return new_member

def display_sorted_birthdays(root):
    all_birthdays = []

    def traverse(node):
        nonlocal all_birthdays
        all_birthdays.append((node.name, node.birthdate))
        for child in node.children:
            traverse(child)

    traverse(root)
    sorted_birthdays = sorted(all_birthdays, key=lambda x: x[1])
    return sorted_birthdays

def find_relationship(node1, node2):
    # Implementing basic logic for finding relationship
    # Assume that node1 is an ancestor of node2
    relationship = ""
    while node2 != node1:
        if not node2:
            relationship = "Not related"
            break
        relationship += "great "
        node2 = node2.parent

    relationship += "ancestor"
    return relationship

def visualize_family_tree(root):
    # The code for visualizing the family tree remains the same

def count_same_first_names(root, first_name):
    count = 0

    def traverse(node):
        nonlocal count
        if node.name.split()[0].lower() == first_name.lower():
            count += 1
        for child in node.children:
            traverse(child)

    traverse(root)
    return count

# Example usage:
root_member = FamilyMember("John Doe", "Doe", "1990-01-01")

while True:
    print("- - - - - - - - - - - - - - -")
    print("1. Add Family Member")
    print("2. Display Sorted Birthdays")
    print("3. Find Relationship")
    print("4. Visualize Family Tree")
    print("5. Count Same First Names")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter member's name: ")
        family_name = input("Enter member's family name: ")
        birthdate = input("Enter member's birthdate (YYYY-MM-DD): ")
        parent_name = input("Enter parent's name: ")

        # Find parent node
        parent_node = None
        queue = [root_member]

        while queue:
            current = queue.pop(0)
            if current.name.lower() == parent_name.lower():
                parent_node = current
                break
            queue.extend(current.children)

        if parent_node:
            new_member = add_family_member(parent_node, name, family_name, birthdate)
            new_member.parent = parent_node
        else:
            print("Parent not found.")

    elif choice == 2:
        sorted_birthdays = display_sorted_birthdays(root_member)
        for name, birthdate in sorted_birthdays:
            print(f"{name}: {birthdate}")

    elif choice == 3:
        # Implement the logic to find the relationship between two nodes
        pass

    elif choice == 4:
        visualize_family_tree(root_member)

    elif choice == 5:
        first_name = input("Enter the first name to count: ")
        count = count_same_first_names(root_member, first_name)
        print(f"There are {count} family members with the first name '{first_name}'.")

    elif choice == 6:
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
