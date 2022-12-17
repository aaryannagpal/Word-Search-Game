def wordsearch(puzzle: list, wordlist: list) -> None:
    if valid_puzzle(puzzle) and valid_wordlist(wordlist): #checking the validity
        positions = []
        for word in wordlist:  #for each word in wordlist
            temp = get_positions(puzzle, word)
            positions.append(temp)
        coloured_display(puzzle, positions)
    else:
        raise ValueError("Invalid puzzle or Wordlist") #raising the exception mentioned


def valid_puzzle(puzzle: list) -> bool:
    x=len(puzzle[0]) #storing length of any string (first in this case) in x
    #if the puzzle is valid, all the lengths should be the same.
    for i in puzzle:
        if len(i)!=x:    #comparing length of all the strings with the first one
            return False #if any is unequal, False is returned
    return True


def valid_wordlist(wordlist: list) -> bool:
    for i in wordlist: 
        if isinstance(i,str): #check if every element in the list is a string
            continue
        else: #if not, return False
            return False
    return True


def get_positions(puzzle: list, word: str) -> list:
    word = word.upper() #converting all the letters to UpperCase
    Location = [] #to store the list of coordinates

    #Iterating over each row, column and diagonal

    #for rows
    for i in range(len(puzzle)):
        row = ''.join(puzzle[i]) #making the whole row into a single string
        row = row.upper() #changing the case of the row-string to match our the word's case
        location = [] #to store the coordinates for single occurance of the word (This is same every time this variable is initialized)
        if word in row: #if our word is in the newly made row-string, then only we will move forward for the locations
            #for word
            x = row.find(word) #finding the starting index of the word in the row
            for j in range(len(word)): #for the length of the word, we update the coordinates in the direction of the word in the row
                location.append((j+x,i)) #here, the direction is from left to right, hence only x-axis is changing. We update the coordinate of each letter to the list
            Location.append(location) #the list of the whole word is then added to the outer list, for a single occurance of the object
        elif word[::-1] in row: #if our word was not in the row string, invert it and check again. If found, repeat the steps, otherwise, move on
            #for inverted word
            k = row.find(word[::-1]) #finding the inverted word
            for j in range(len(word)):
                location.append((k+j,i))
            Location.append(location[::-1]) #only difference here is that we added the letter-wise coordinates of the inverted word to the word list.
                                            #Hence, to adjust to that inversion, we invert the word list first and then add.
            #return Location[::-1]

    #for columns
    for i in range(len(puzzle)):
        col = ''
        for j in range(len(puzzle)):
            col += puzzle[j][i] #making the whole column into a single string
            col = col.upper() #changing the case of the column-string to match our the word's case
        location = [] #storing for single occurance
        #making a column into string
        if word in col:
            k = col.find(word) #finding the starting index of the word in the column
            for a in range(len(word)):
                location.append((i,a+k)) #here, the direction is from up to down, hence only y-axis is changing. We update the coordinate of each letter to the list
            Location.append(location)
            #return Location
        elif word[::-1] in col:
            #everything is same for the inverted word, only the word-list is reversed before adding to the main list
            k = col.find(word[::-1])
            for a in range(len(word)):
                location.append((i,a+k))
            Location.append(location[::-1])
            #return Location[::-1]

    #for diagonals going right to left
    #for upper half
    for i in range(len(puzzle)):
        dia = ''
        #introducing 2 pointers to keep track of the movement in the x and y direction, since the search is not fixed on one axis
        pointer_y = i #Will check OVER the largest right to left diagonal by changing the beginning point of the search on the x axis
        pointer_x = 0 #will be used to count the iterations over the columns
        #let there be a search pointer which points over an element, controlled by our 2 pointers given
        #our pointers give that search pointer direction and movement
        while pointer_x <= i: 
            dia+=puzzle[pointer_x][pointer_y] #making the diagonal into a string as well by going over each letter and adding them
            pointer_y-=1 #takes our searching pointer one step left
            pointer_x+=1 #takes our searching pointer one step down
            #for the pointers to find the letter in the diagonal they are in
        dia = dia.upper() #maintaining the case sensitivity
        location = [] #storing for single occurance
        if word in dia:
            #for word
            k = dia.find(word) #finding the starting index of the word in the diagonal
            for a in range(len(word)):
                location.append((i-(k+a),0+k+a)) #updating and adding the coordinates in direction of the search (Upper Right to Lower Left)
            Location.append(location)
            #return Location
        elif word[::-1] in dia:
            #everything is same for the inverted word, only the word-list is reversed before adding to the main list
            k = dia.find(word[::-1])
            for a in range(len(word)):
                location.append((i-(k+a),0+k+a))
            Location.append(location[::-1])
            #return Location[::-1]

    #for lower half
    for i in range(len(puzzle)):
        dia = ''
        pointer_y = len(puzzle)-1 #first our search pointer checked all the diagonals over the largest diagonal.
        pointer_x = i #Now it will check UNDER it by changing the beginning point of the search on the y axis
        while pointer_y >= 0 and pointer_x < len(puzzle): #starting our search from the bottom right 
            dia+=puzzle[pointer_x][pointer_y]
            pointer_x+=1 #since we are searching from bottom right to upper left, we move up by 1 
            pointer_y-=1 #and move left by 1
        dia = dia.upper() #maintaining the case sensitivity
        location = [] #storing for single occurance
        if word in dia:
            #for word
            k = dia.find(word) #finding the starting index of the word in the diagonal
            for a in range(len(word)):
                location.append((len(puzzle)-1-(k+a),i+(k+a))) #updating the coordinates accordingly
            Location.append(location)
            #return Location
        elif word[::-1] in dia:
            #everything is same for the inverted word, only the word-list is reversed before adding to the main list
            k = dia.find(word[::-1])
            for a in range(len(word)):
                location.append((len(puzzle)-1-(k+a),i+(k+a)))
            Location.append(location[::-1])
            #return Location[::-1]

    #for diagonals going left to right
    #for upper half
    for i in range(len(puzzle)-1,-1,-1):
        dia = ''
        pointer_y = i #Will check OVER the largest left to right diagonal by changing the beginning point of the search on the x axis
        pointer_x = 0 #will be used to count the iterations over the columns
        while pointer_y < len(puzzle):
            dia+=puzzle[pointer_x][pointer_y] #making the diagonal into a string as well by going over each letter and adding them
            pointer_y+=1 #since our search is from upper left to bottom right, we take our pointer one step down
            pointer_x+=1 #and one step right
        dia = dia.upper() #maintaining the case sensitivity
        location = [] #storing for single occurance
        if word in dia:
            #for word
            k = dia.find(word) #finding the starting index of the word in the diagonal
            for a in range(len(word)):
                location.append((i+(k+a),0+k+a)) #updating and adding the coordinates in direction of the search (Upper Left to Lower Right)
            Location.append(location)
            #return Location
        elif word[::-1] in dia:
            #everything is same for the inverted word, only the word-list is reversed before adding to the main list
            k = dia.find(word[::-1])
            for a in range(len(word)):
                location.append((i+(k+a),0+k+a))
            Location.append(location[::-1])
            #return Location[::-1]

    #for lower half
    for i in range(len(puzzle)):
        dia = ''
        pointer_x = i #Will check UNDER the largest left to right diagonal by changing the beginning point of the search on the x axis
        pointer_y = 0 #will be used to count the iterations over the rows
        while pointer_x < len(puzzle) and pointer_y < len(puzzle):
            dia+=puzzle[pointer_x][pointer_y] #making the diagonal into a string as well by going over each letter and adding them
            pointer_y+=1 #since our search is from upper left to bottom right, we take our pointer one step down
            pointer_x+=1 #and one step right
        dia = dia.upper() #maintaining the case sensitivity
        location = [] #storing for single occurance
        if word in dia:
            #for word
            k = dia.find(word) #finding the starting index of the word in the diagonal
            for a in range(len(word)):
                location.append((0+k+a,i+(k+a))) #updating and adding the coordinates in direction of the search (Upper Left to Lower Right)
            Location.append(location)
            #return Location
        elif word[::-1] in dia:
            #everything is same for the inverted word, only the word-list is reversed before adding to the main list
            k = dia.find(word[::-1])
            for a in range(len(word)):
                location.append((0+k+a,i+(k+a))) #updating and adding the coordinates in direction of the search (Upper Left to Lower Right)
            Location.append(location[::-1])
            #return Location[::-1]


    result = []
    for i in Location:
        if i not in result: #to avoid the repetition due to looping
            result.append(i)
    return result


def basic_display(grid: list) -> None:
    for i in grid:
        for j in i: #pick every element and print it with a seperation
            print(j.upper(),end='\t') # '\t' can be replaced with ' '. \t is just wider.
        print('\n') #change line after every line


def coloured_display(grid: list, positions: list) -> None:
    #converting the input (list of strings --> list of lists),
    for i in range(len(grid)):
        x = [j.upper() for j in grid[i]] #converting the string to list, while maintaining a standard case sensitivity
        grid[i] = x #so that we can easily replace the elements
        
    for i in positions: #going over the word-wise coordinates found for our words
        for j in i: #going over for each occurance of that word
            for k in j: #going over each coordinate in that occurance
                x,y = k #locating each element at that coordinate
                if "[42m" in grid[y][x]:
                    pass #if the element has been already painted green in any previous iteration, then dont repeat the paint
                else:
                    f = "\033[42m "+grid[y][x]+" \033[0m" #changing the element to green
                    grid[y][x] = f #replace the element with the green element
                #print(grid[x][y]) #to debug
    
    for i in grid: #pick every element and print it with a seperation
        for j in i:
            print(j ,end='\t')
        print('\n')#change line after every line
    pass

#--------------------------------------------------------------------------------------#



puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

wordlist = ["scalar", "tray", "blew", "sevruc"]

wordsearch(puzzle, wordlist)
