import anytree


class FamilyTree:

    def __init__(self):
        # ex: self.name = anytree.Node("")
        self.lucille = anytree.Node("Lucille")
        self.buster = anytree.Node("Buster")
        self.lindsay = anytree.Node("Lindsay")
        self.george_oscar = anytree.Node("George Oscar")
        self.michael = anytree.Node("Michael")
        self.maeby = anytree.Node("Maeby")
        self.george_michael = anytree.Node("George Michael")
        return

    def populate_family_tree(self):
        # ex: child = Node('My Name', parent = parent_node)
        self.buster = anytree.Node('Buster', parent=self.lucille)
        self.lindsay = anytree.Node('Lindsay', parent=self.lucille)
        self.george_oscar = anytree.Node('George Oscar', parent=self.lucille)
        self.michael = anytree.Node('Michael', parent=self.lucille)
        self.maeby = anytree.Node('Maeby', parent=self.lindsay)
        self.george_michael = anytree.Node('George Michael', parent=self.michael)
        # FIXME!
        return
