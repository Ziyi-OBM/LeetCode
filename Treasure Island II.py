https://leetcode.com/discuss/interview-question/356150/amazon-oa-2019-treasure-island-ii

input2D=[
['S', 'O', 'O', 'S', 'S'],
['D', 'O', 'D', 'O', 'D'],
['O', 'O', 'O', 'O', 'X'],
['X', 'D', 'D', 'O', 'O'],
['X', 'D', 'D', 'D', 'O'],
]
    
row=len(input2D)
col=len(input2D[0])
shortest=row+col-2
numNode=row*col

##My first implementation
##Queue implementation, use label[x] to keep track of distance. Increment dist[child]=dist[parent]+1

for i in range(row):
    for j in range(col):
        if input2D[i][j]=='S':        
        #####################################################################
            queue=[row*i+j]
            label={queue[0]:0}
            prev = {queue[0]:None}
            cursor=0
            dist=1

            while cursor != len(queue):
                newj=int(queue[cursor]%row)
                newi=int((queue[cursor]-newj)/row)                
                dist=label[queue[cursor]] 
                           
                if input2D[newi][newj]=='X':
                    if dist<shortest:
                        shortest=dist
                    break                                    
                for x,y in ((newi-1,newj),(newi+1,newj),(newi,newj-1),(newi,newj+1)):                     
                    if x>=0 and x<row and y>=0 and y<col and (input2D[x][y]!='D') and not(row*x+y in label):                        
                        queue.append(row*x+y)
                        label[row*x+y]=label[queue[cursor]]+1
                        prev[row*x+y]=queue[cursor]                      
                cursor=cursor+1       
print(shortest)

                    
### Another implementation:
### Loop over all nodes in the same level and move to the next level
### 'sameLvl' Contains all nodes in the current level
### Assign distances as dist[new node]=level and increment level after finishing all nodes in this level
for iS in range(1):
    for jS in range(1):   
        if input2D[iS][jS]=='S': 
            level=1
            frontier=[row*iS+jS]
            found=0
            dist={row*iS+jS:0}
            while frontier:
                sameLvl=[]
                for node in frontier:
                    jF=int(node%row)
                    iF=int((node-jF)/row) 
                        
                    for i,j in ((iF-1,jF),(iF+1,jF),(iF,jF+1),(iF,jF-1)):
                        if i>=0 and i<row and j>=0 and j<col and (input2D[i][j]!='D') and not(row*i+j in dist):
                            sameLvl.append(i*row+j)
                            dist[i*row+j]=level
                            print(i,j,level)
                            if input2D[i][j]=='X':
                                found=1
                                if level < shortest:
                                    shortest=level
                                break                                                            
                    if found == 1:
                        break
                if found == 1:
                    found=0
                    break
                    
                frontier = sameLvl
                level=level+1
                
                
                
print(shortest)

            