def print_christmas_tree():
  # First, define the height of the tree
  tree_height = 5

  # Next, print the top of the tree
  print(" " * (tree_height - 1) + "*")

  # Then, print the rest of the tree
  for i in range(1, tree_height):
    # Calculate the number of spaces and stars for this row
    num_spaces = tree_height - i
    num_stars = (i * 2) - 1

    # Print the row
    print(" " * num_spaces + "*" * num_stars)

  # Finally, print the base of the tree
  print(" " * (tree_height - 2) + "***")


# Test the function
print_christmas_tree()
