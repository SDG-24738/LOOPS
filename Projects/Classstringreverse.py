class reverse:
    def __init__(self, s):
        self.s = s
    def reversestring(self):
        for x in range(len(self.s)-1, -1, -1):
            print(self.s[x])
revstrng = reverse("Shashank")
revstrng.reversestring()