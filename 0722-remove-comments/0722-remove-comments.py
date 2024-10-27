class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        commenting=False
        modified=''
        ans=[]
        for line in source:
            i=0
            while(i<len(line)):
                if i+1==len(line):
                    if not commenting:
                        modified+=line[i]
                    break
                twochars=line[i:i+2]
                if twochars=="/*" and not commenting:
                    commenting=True
                    i+=2
                elif twochars=="*/" and commenting:
                    commenting=False
                    i+=2
                elif twochars=="//":
                    if not commenting:
                        break
                    if commenting:
                        i+=2
                else:
                    if not commenting:
                        modified+=line[i]
                    i+=1
            if not commenting:
                if len(modified)!=0:
                    ans.append(modified)
                modified=''
        return ans


