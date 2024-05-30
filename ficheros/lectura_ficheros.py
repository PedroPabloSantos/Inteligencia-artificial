# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:02:10 2024

@author: Pedro Pablo
"""
import pandas as pd
import numpy as np

def lectura_titanic():
    fichero = pd.read_csv('titanic.csv', na_values=-1)    
    return fichero

def lectura_titanic_separado():
    fichero = pd.read_csv('titanic.csv', na_values=-1)
    atributos_discretos = ['Sex', 'Embarked', 'Alone', 'Deck']
    atributos_continuos = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Initial', 
                           'Age_band', 'Family_Size', 'Fare_cat', 'Title', 'Is_Married']
    atributos = fichero.loc[:, atributos_discretos + atributos_continuos]
    objetivo = fichero['Survived']
    return atributos, objetivo


def lectura_breastCancer():
    fichero = pd.read_csv('BreastCancer.csv', na_values=-1)
    return fichero

def lectura_breastCancer_separado():
    fichero = pd.read_csv('BreastCancer.csv', na_values=-1)
    atributos_continuos = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 
                           'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension', 'radius error', 
                           'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error',
                           'concave points error', 'symmetry error', 'fractal dimension error', 'worst radius', 'worst texture', 
                           'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points',
                           'worst symmetry', 'worst fractal dimension']
																				
    atributos = fichero.loc[:, atributos_continuos]
    objetivo = fichero['diagnosis']
    return atributos, objetivo


print(lectura_titanic_separado())
print(lectura_breastCancer_separado())

