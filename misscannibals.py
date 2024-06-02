from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)
        
    def actions(self, state):
        M, C, boat = state
        possible_actions = []
        if boat:  #boat is on the starting side
            if M >= 2:
                possible_actions.append('MM')
            if C >= 2:
                possible_actions.append('CC')
            if C >= 1:
                possible_actions.append('C')
            if M >= 1:
                possible_actions.append('M')
            
            if M >= 1 and C >= 1:
                possible_actions.append('MC')
        else:  #boat is on the other side
            if self.M - M >= 2:
                possible_actions.append('MM')
            if self.C - C >= 2:
                possible_actions.append('CC')
            if self.C - C >= 1:
                possible_actions.append('C')
            if self.M - M >= 1:
                possible_actions.append('M')
            if self.M - M >= 1 and self.C - C >= 1:
                possible_actions.append('MC')

    
        return possible_actions

    


	
if __name__ == '__main__':
    mc = MissCannibals(3,3)
    print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']
	
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
