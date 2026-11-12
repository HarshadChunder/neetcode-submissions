class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet_arrival_times = []

        for car_position, car_speed in cars:
            arrival_time = (target - car_position) / car_speed
            if not fleet_arrival_times or arrival_time > fleet_arrival_times[-1]:
                fleet_arrival_times.append(arrival_time)

        return len(fleet_arrival_times)