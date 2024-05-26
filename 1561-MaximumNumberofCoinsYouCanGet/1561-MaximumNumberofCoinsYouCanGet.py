        sorted_pile = sorted(piles, reverse=True)
        last_pile = len(sorted_pile)-1
        i = 0
        mycoins = 0
        while((i+2)<=last_pile):

            mycoins += sorted_pile[i+1]
            i = i+2
            last_pile -= 1

    def maxCoins(self, piles: List[int]) -> int:

[
