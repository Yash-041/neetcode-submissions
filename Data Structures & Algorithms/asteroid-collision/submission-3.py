class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state = []

        for a in asteroids:
            while state and a < 0 and state[-1] > 0:
                diff = a + state[-1]
                if diff < 0:
                    state.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    state.pop()
            if a:
                state.append(a)

        return state
