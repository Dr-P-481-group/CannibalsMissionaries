from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)
    
    def valid_state(self, state):
      M, C, boat = state
      return (0 <= M <= self.M and 0 <= C <= self.C and (M == 0 or M >=C) and (self.M - M == 0 or self.M - M >= self.C - C))
    
    def actions(self, state):
        M, C, boat = state
        possibleActions = []
        if boat:  # boat is on the starting side
            if M >= 2:
                possibleActions.append('MM')
            if C >= 2:
                possibleActions.append('CC')
            if C >= 1:
                possibleActions.append('C')
            if M >= 1:
                possibleActions.append('M')
            if M >= 1 and C >= 1:
                possibleActions.append('MC')
        else:  # boat is on the other side
            if self.M - M >= 2:
                possibleActions.append('MM')
            if self.C - C >= 2:
                possibleActions.append('CC')
            if self.C - C >= 1:
                possibleActions.append('C')
            if self.M - M >= 1:
                possibleActions.append('M')
            if self.M - M >= 1 and self.C - C >= 1:
                possibleActions.append('MC')
        
        valid_actions = []
        for action in possibleActions:
          new_state = self.result(state, action)
          if(self.valid_state(new_state)):
            valid_actions.append(action)
        return valid_actions
                                
    def result(self, state, action):
        M, C, boat = state
        new_state = ()
              
        if action == 'MM':
            new_state = (M - 2, C, not boat) if boat else (M + 2, C, not boat)
        elif action == 'CC':
            new_state = (M, C - 2, not boat) if boat else (M, C + 2, not boat)
        elif action == 'C':
            new_state = (M, C - 1, not boat) if boat else (M, C + 1, not boat)
        elif action == 'M':
            new_state = (M - 1, C, not boat) if boat else (M + 1, C, not boat)
        elif action == 'MC':
            new_state = (M - 1, C - 1, not boat) if boat else (M + 1, C + 1, not boat)
        return new_state
                        
    def goal_test(self, state):
        return state == self.goal
		    
if __name__ == '__main__':
    mc = MissCannibals(3, 3)
    print(mc.actions((3, 2, True)))  # Expected Output -> ['CC', 'C', 'M']
    print(mc.actions((1, 1, False)))
	
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
