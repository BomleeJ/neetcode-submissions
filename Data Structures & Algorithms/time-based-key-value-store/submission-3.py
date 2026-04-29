class TimeMap:

    def __init__(self):
        #Dict[t, Dict[k, v]]
        self.mdict = dict()
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mdict.get(key):
            self.mdict[key].append([value, timestamp])
        else:
            self.mdict[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        actions, res = self.mdict.get(key, []), ""
        l, r = 0, len(actions) - 1 
        while l <= r:
            mid = l + ((r - l) // 2)
            if actions[mid][1] <= timestamp:
                res = actions[mid][0]
                l = mid + 1
            elif actions[mid][1] > timestamp:
                r = mid - 1

        return res

        
        

            


        

        
        
            

        
        
