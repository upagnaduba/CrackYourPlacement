class Solution(object):
    def isCircularSentence(self, sentence):
        Flag=False
        if sentence[0]==sentence[-1]:
            Flag=True
        for i in range(len(sentence)):
            if sentence[i]==" ":
                if sentence[i-1]!=sentence[i+1]:
                    Flag=False
        
        return Flag
        