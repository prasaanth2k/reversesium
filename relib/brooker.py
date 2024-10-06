class BROOKER:

    def patterngenerater(self,counts):
        # Basic Pattern is below 
        # aA0aA1aA2aA3 <--> zZ9
        # So total we can generate 
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        captial_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        pattern = small_letters[0]+captial_letters[0]+numbers[0]
        print(pattern)
        print(counts)

