# General Tree

class TreeNode:
    def __init__(self,data) -> None:
        self.data =  data
        self.children = []
        self.parent = None


    def __str__(self):
        spaces = "    " * self.get_level() * 3
        print( spaces + "|__" + str(self.data))
        if self.children:
            for i in self.children:
                i.__str__()
        
        return ""

    def get_level(self):
        # just count the no of ancestors
        level =0
        p = self.parent
        while p:
            level+=1
            p= p.parent
        return level

    def add_child(self,child):
        child.parent= self
        self.children.append(child)
        

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    cellPhone = TreeNode("Cell Phone")
    cellPhone.add_child(TreeNode('IPHONE'))
    cellPhone.add_child(TreeNode("Google Pixel"))
    cellPhone.add_child(TreeNode("VIVO"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))


    root.add_child(laptop)
    root.add_child(cellPhone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    print(root)