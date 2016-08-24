import matplotlib.pyplot as plt
from IBP import IBP


alpha=range(1,12,2)
 #Vary alpha
fig = plt.figure()
#fig.set_size_inches(24, 50)
ax=fig.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
ax.set_xlabel('Number of Dishes')
ax.set_ylabel('Number of Customers')
ax.set_title('Variation of Alpha Parameter for the IBP\n\n',fontsize=18)
for j in range(1,7):
    im = IBP(20,alpha[j-1]);
    fig.add_subplot(2,3,j)
    ax=plt.imshow(im,'gray',interpolation='none') 
    plt.title('alpha = '+str(alpha[j-1]))
plt.tight_layout()    
plt.show()
fig.savefig('Alpha.png')

#Vary number of data points
N=range(10,120,20);
fig = plt.figure()
ax=fig.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
ax.set_xlabel('Number of Dishes')
ax.set_ylabel('Number of Customers')
ax.set_title('Variation of the Number of Customers in an IBP\n\n',fontsize=18)
for j in range(1,7):
    im = IBP(N[j-1],10);
    fig.add_subplot(2,3,j)
    plt.imshow(im,'gray',interpolation='none')
    plt.title('N = '+str(N[j-1]))
plt.tight_layout() 
plt.show()
fig.savefig('N.png')

