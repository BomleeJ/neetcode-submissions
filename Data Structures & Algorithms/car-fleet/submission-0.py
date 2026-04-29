class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create m remaining array
        # sort m remaining from smallest to largest

        distance = [target - current_position for current_position in position]
        cars = list(zip(distance, speed))

        cars.sort(key=lambda x: x[0])

        ETAs = [dist / speed for dist, speed in cars]
        maxi = 0
        fleet = 0
        for idx in range(len(ETAs)):
            if ETAs[idx] > maxi:
                maxi = ETAs[idx]
                fleet += 1

        return fleet


        # if the remaining distance between two ca



        # sort the array 
        # after every tick we can apply the speeds and recalculate
        # we have a fleet when two cars are the same distance from the target at which point the window opens and