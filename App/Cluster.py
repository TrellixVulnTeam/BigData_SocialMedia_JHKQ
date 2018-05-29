import math
import random
import time 
import sys
import decimal
#import matplotlib.pyplot as plt

#Tweets data source
data_file = "text.json"


# Possible number of data points
n = len(data_file)
#my end condition
global Epsilion 
Epsilion = 0.000001

#Assign default static Number of Clusters as alternative
k = 2

#set Fuzzy parameter
m = 2.00


#function to import the data set from file, i will split the data using , or space
def import_data(sourceFile):
    data = []
    f = open(str(sourceFile), 'r')
    for line in f:
        current = line.split(" ") #split by space
        for j in range(0, len(current)):
            current[j] = int(current[j])
        data.append(current)
    
    return data 


#function to print my matrix in order to visiualize it
def display_matrix(list):
    for i in (0, len(list)):
        print (list[i])

#function to initialize the member matrix, give random list it may be incorrect but later will be modofied
def initializeMembershipMatrix():
    membership_mat = list()
    for i in range(n):
        random_num_list = [random.random() for i in range(k)]
        summation = sum(random_num_list)
        temp_list = [x/summation for x in random_num_list]
        membership_mat.append(temp_list)
    return membership_mat

#update the member grade interatively, this tries to move data set closer to desired cluster
def updateMembershipValue(membership_mat, cluster_centers):
    p = float(2/(m-1))
    for i in range(n):
        distances = [range(k)]
        for j in range(k):
            den = sum([math.pow(float(distances[j]/distances[c]), p) for c in range(k)]) #denisty range
            membership_mat[i][j] = float(1/den)       
    return membership_mat

#finding my cluster center
def calculateClusterCenter(membership_mat):
    cluster_centers = list()
    for j in range(k):
        x = list()
        xraised = [e ** m for e in x] #get raised value
        denominator = sum(xraised)
        temp_num = list()
        for i in range(n):
            data_point = list()
            prod = [xraised[i] * val for val in data_point]
            temp_num.append(prod)
        numerator = map(sum, zip(*temp_num))
        center = [z/denominator for z in numerator]
        cluster_centers.append(center)
    return cluster_centers

def findClusters(membership_mat):
    cluster_labels = list()
    for i in range(n):
        idx = max((val, idx) for (idx, val) in enumerate(membership_mat[i]))
        cluster_labels.append(idx)
    return cluster_labels

def fuzzyCMeansClustering():
    # Membership Matrix
    membership_mat = initializeMembershipMatrix()
    curr = 0
    while curr <= 10:
        cluster_centers = calculateClusterCenter(membership_mat)
        membership_mat = updateMembershipValue(membership_mat, cluster_centers)

        curr += 1
        print(membership_mat[curr])
    


print (fuzzyCMeansClustering)
