#Current code is solution of codility for the problem of combination split of a and b strings.
# Ranging from 0 , 40000

solution(s):
	count = [0] * 4000; 
    	# what will find frequency of each character 
    	for x in s: 
        count[ord(x) - ord('a')] = (count[ord(x) - ord('a')]) + 1; 


    	# first character frequency
    	count[ord(s[0]) - ord('a')] = 1; 

    	# occurrence of each character
    	count_split = 1; 
    	for i in range(4000): 
        		if (count[i] != 0): 
            	count_split *= count[i]; 
  
    	return count_split; 

if __name__ == '__main__': 
    s = "acbbcc"; 
    print(solution(s));
