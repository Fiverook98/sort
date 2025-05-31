class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []
  
  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)

    while story_node.choices:
      choice = int(input("Choose your destiny... [1] or [2]"))

      if choice in [1, 2]:
        chosen_child = story_node.choices[choice - 1]

      else:
        print("Invalid choice! Retry.")
        
      print(chosen_child.story_piece)
      story_node = chosen_child
    
    print("The story is at the end!")