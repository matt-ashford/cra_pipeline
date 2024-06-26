
import pandas as pd
import numpy as np
import os

class FileIO:
    @staticmethod
    def exportFile(frame, fileName):
        path = "./finalTables/"
        fullPath = os.path.join(path, fileName)
        frame.to_csv(fullPath, index=False)

    @staticmethod
    def importFile(fileName):
        path = "./finalTables/"
        fullPath = os.path.join(path, fileName)
        frame = pd.read_csv(fullPath)
        return frame
    
    @staticmethod
    def importKey():
        keyPath = r"C:\Users\matthew.ashford\OneDrive - Postal Regulatory Commission\Documents\AA documents/Data initiatives/Postal Database"
        keyFileName = "product Id key.csv"
        fullKeyPath = os.path.join(keyPath, keyFileName)
        keyFrame = pd.read_csv(fullKeyPath)
        return keyFrame
    
class DataframeCleaning:
    @staticmethod
    def realignWithKey(frame, keyFrame=None):
        if keyFrame is None:
            keyFrame = FileIO.importKey()
        toMerge_values = frame.copy()
        dropFromValues = ["product", "mail_class"]
        for col in dropFromValues:   
            if col in toMerge_values.columns:
                toMerge_values.drop(col,axis=1,  inplace=True)
        keyCols = ['product_id', 'product','mail_class']
        toMerge_keys = keyFrame[keyCols]
        mergedFrame = pd.merge(toMerge_values, toMerge_keys, how='left', on='product_id')
        leadingCols = keyCols + ["fy"]
        remainingCols  = [c for c in frame.columns if c not in leadingCols]
        orderedCols = leadingCols + remainingCols
        return mergedFrame[orderedCols]
    
    
    

            
    



