'''
Created on Feb 25, 2016

@author: xiayuanhuang
'''


#import decisionTreeV3
#import family_treeV2
import sys
import decisionTreeV6
import family_treeV4

def main(addressFile, nameFile, demoFile, accountFile, outputFile, familyTreeOutput):
    ''' 
        input arguments: 
        addressFile:     address_deid.csv   
        nameFile:        name_deid.csv    
        demoFile:        demo_deid.csv    
        accountFile:     account_deid.csv
    '''
#     addressFile = 'address_deid.csv'
#     nameFile = 'name_deid.csv'
#     demoFile = 'demo_deid.csv'
#     accountFile = 'account_deid.csv'

    ''' 
        an intermediate output txt file for predicted parent-child relationship and input file 
        for family_tree construction.
        e.g. p_c.txt 
    '''
#     outputFile = 'p_c3.txt'
    
    '''
        an output csv file for predicted families
        e.g. family_tree.csv
    '''
#     familyTreeOutput = 'family_tree.csv'
    
    '''
        predict parent-child relationship
    '''
    newDT = decisionTreeV6.DT(addressFile, nameFile, demoFile, accountFile)
    newDT.predict()
    newDT.writeToFile(outputFile)
    
    '''
        predict families with input of parent-child relationship data
    '''
    
    newFamilyTree = family_treeV4.familyTree(newDT)
    #newFamilyTree = family_treeV4.familyTree(addressFile, nameFile, demoFile, accountFile)
    newFamilyTree.filter(outputFile)
    newFamilyTree.buildTree()
    newFamilyTree.connected(familyTreeOutput)
    

if __name__ == "__main__":
    '''
        6 arguments
        
        sys.argv[1]    addressFile:     address_deid.csv   
        sys.argv[2]    nameFile:        name_deid.csv    
        sys.argv[3]    demoFile:        demo_deid.csv    
        sys.argv[4]    accountFile:     account_deid.csv
        
        sys.argv[5]    an intermediate output txt file for predicted parent-child relationship and input file 
                       for familiy_tree construction.
                       e.g. p_c.txt  (child, parent)
        
        sys.argv[6]    an output csv file for predicted families
                       e.g. family_tree.csv
                       
        ['address_deid.csv', 'name_deid.csv', 'demo_deid.csv', 'account_deid.csv', 'p_c.txt', 'family_tree.csv']
        
    '''
    print(len(sys.argv))
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
