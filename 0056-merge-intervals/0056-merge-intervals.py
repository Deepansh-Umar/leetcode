class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        start1=intervals[0][0]
        end1 = intervals[0][1]
        rs = [[start1,end1]]
        for s,e in intervals:
            start1=rs[-1][0]
            end1 = rs[-1][1]
            if s>end1:
                rs.append([s,e])
                continue
            if s>= start1 and e<= end1:
                continue
            elif s>= start1 and e> end1:
                rs[-1][1]=e
        return rs

            
            
