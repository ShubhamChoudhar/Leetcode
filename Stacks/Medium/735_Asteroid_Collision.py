class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        new_asteroids = []

        if len(asteroids) == 0:
            return []
        if len(asteroids) == 1:
            return asteroids

        for asteroid in asteroids:
            if len(new_asteroids) == 0:
                new_asteroids.append(asteroid)
            elif asteroid < 0:
                while new_asteroids and new_asteroids[-1] > 0:
                    if abs(new_asteroids[-1]) < abs(asteroid):
                        new_asteroids.pop()

                    elif abs(new_asteroids[-1]) == abs(asteroid):
                        new_asteroids.pop()
                        break

                    else:
                        break

                else:
                    new_asteroids.append(asteroid)
            
            else:
                new_asteroids.append(asteroid)
        
        return new_asteroids

        # new_asteroids = []

        # for asteroid in asteroids:
            # If the current asteroid is moving right or there are no asteroids in the stack 
            # or the top asteroid in the stack is moving left, just append the current asteroid.
            # if asteroid > 0 or not new_asteroids or new_asteroids[-1] < 0:
                # new_asteroids.append(asteroid)
            # If the current asteroid is moving left and the top asteroid in the stack is moving right
            # elif new_asteroids[-1] > 0:
                # While there are asteroids in the stack and the top one is moving right
                # while new_asteroids and new_asteroids[-1] > 0:
                    # If the top asteroid in the stack is smaller in magnitude, pop it.
                    # if new_asteroids[-1] < -asteroid:
                        # new_asteroids.pop()
                    # If they are equal in magnitude, pop the top one and break (as the current one is also destroyed).
                    # elif new_asteroids[-1] == -asteroid:
                    #     new_asteroids.pop()
                    #     break
                    # If the top asteroid in the stack is larger in magnitude, just break (as the current one is destroyed).
                    # else:
                    #     break
                # If there are no asteroids left in the stack or the top one is moving left, append the current asteroid.
        #         else:
        #             new_asteroids.append(asteroid)

        # return new_asteroids

# asteroids = [5, 10, -5]
asteroids = [8, -8]
# asteroids = [-2, -1, 1, 2]
# asteroids = [2, 2, 1, -3]
# asteroids = [10, 2, -5]
print(Solution().asteroidCollision(asteroids))