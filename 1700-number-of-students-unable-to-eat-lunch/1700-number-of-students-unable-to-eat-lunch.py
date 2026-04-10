class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c=0
        i=0
        while(students):
            if c==len(students):
                return c
            v = students[0]
            s = sandwiches[i]
            if v==s:
                students.pop(0)
                i+=1
                c=0
            else:
                students.append(students.pop(0))
                c+=1
        return len(students)