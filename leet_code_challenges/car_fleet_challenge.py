from typing import List;


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = [0]
        for idx in range(1,len(position)):
            pos_val = position[idx]
            speed_val = speed[idx]
            time_taken = (target-pos_val)/speed_val
      
            
            temp_arr = []

            while stack:
                top_stack_pos = position[stack[-1]]
                top_stack_speed = speed[stack[-1]]

                if top_stack_pos > pos_val and top_stack_speed < speed_val:
                    catch_up_time = (top_stack_pos-pos_val)/(speed_val-top_stack_speed)

                    time_taken_by_top_stack = (target-top_stack_pos)/top_stack_speed

                    if catch_up_time <= time_taken_by_top_stack:
                        break

                elif top_stack_pos < pos_val and top_stack_speed > speed_val:
                    catch_up_time = (pos_val-top_stack_pos)/(top_stack_speed-speed_val)
                    if catch_up_time <= time_taken:
                        stack.pop()
                        continue
              
                temp_arr.append(stack.pop())

            if len(stack) == 0:
                temp_arr.insert(0,idx)
            for val in temp_arr:
                stack.insert(0,val)



        return len(stack)



target = 12
position = [10,8,0,5,3]
speed =[2,4,1,1,3]


print(Solution().carFleet(target,position,speed))

target = 16
position = [11,14,13,6]
speed = [2,2,6,7]

print(Solution().carFleet(target,position,speed))


target = 100
position = [0,2,4]
speed = [4,2,1]

print(Solution().carFleet(target,position,speed))

target = 10
position = [0,4,2]
speed = [2,1,3]

print(Solution().carFleet(target,position,speed))

target = 13
position = [10,2,5,7,4,6,11]
speed = [7,5,10,5,9,4,1]
print(Solution().carFleet(target,position,speed))